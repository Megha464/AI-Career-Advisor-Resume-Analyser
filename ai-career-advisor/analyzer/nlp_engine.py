"""
NLP & Semantic Analysis Engine.
Calculates semantic similarity, skill extractions, role matching, missing skills,
personalized learning roadmaps, recommended projects, interview questions, and readiness scores.
"""

import re
from typing import Dict, Any, List, Set
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .skills_db import SKILLS_TAXONOMY, SKILL_ALIASES
from .roles_db import CAREER_ROLES

def extract_skills_from_text(text: str) -> Dict[str, List[str]]:
    """
    Scans text for skills from the taxonomy and alias dictionary.
    Returns detected skills grouped by category and flat set.
    """
    text_lower = text.lower()
    # Normalize punctuation for safer boundary matching
    normalized_text = " " + re.sub(r'[^\w\s\+\#\.]', ' ', text_lower) + " "

    detected_by_category: Dict[str, Set[str]] = {cat: set() for cat in SKILLS_TAXONOMY}
    all_detected: Set[str] = set()

    for category, skill_list in SKILLS_TAXONOMY.items():
        for skill in skill_list:
            skill_clean = skill.lower()
            # Escape regex characters
            pattern = rf'(?:\b|\s){re.escape(skill_clean)}(?:\b|\s)'
            if re.search(pattern, normalized_text):
                detected_by_category[category].add(skill)
                all_detected.add(skill)

    # Check aliases
    for alias, canonical in SKILL_ALIASES.items():
        pattern = rf'(?:\b|\s){re.escape(alias)}(?:\b|\s)'
        if re.search(pattern, normalized_text):
            all_detected.add(canonical)
            # Find category of canonical
            for cat, s_list in SKILLS_TAXONOMY.items():
                if canonical in s_list:
                    detected_by_category[cat].add(canonical)

    # Convert sets to sorted lists
    return {
        "by_category": {cat: sorted(list(skills)) for cat, skills in detected_by_category.items() if skills},
        "all_skills": sorted(list(all_detected))
    }

def calculate_semantic_similarity(text1: str, text2: str) -> float:
    """Calculates TF-IDF cosine similarity between two texts (returns float 0.0 - 1.0)."""
    if not text1.strip() or not text2.strip():
        return 0.0
    try:
        vectorizer = TfidfVectorizer(stop_words='english', max_features=1500)
        tfidf = vectorizer.fit_transform([text1, text2])
        sim = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
        return float(np.clip(sim, 0.0, 1.0))
    except Exception:
        return 0.35

def calculate_resume_job_match(resume_text: str, resume_skills: List[str], jd_text: str) -> Dict[str, Any]:
    """
    Computes detailed match analysis between candidate resume and target Job Description.
    """
    jd_skills_data = extract_skills_from_text(jd_text)
    jd_skills = jd_skills_data["all_skills"]
    
    resume_skills_set = set(resume_skills)
    jd_skills_set = set(jd_skills)
    
    # Matched vs Missing skills
    matched_skills = sorted(list(resume_skills_set.intersection(jd_skills_set)))
    missing_skills = sorted(list(jd_skills_set.difference(resume_skills_set)))
    
    # Skill match ratio
    if len(jd_skills_set) > 0:
        hard_skill_ratio = len(matched_skills) / len(jd_skills_set)
    else:
        hard_skill_ratio = 0.70  # default baseline if JD has non-standard skills
        
    # Semantic text similarity
    semantic_sim = calculate_semantic_similarity(resume_text, jd_text)
    
    # Soft skills match
    resume_soft = set(s for s in resume_skills if s in SKILLS_TAXONOMY.get("soft_skills", []))
    jd_soft = set(s for s in jd_skills if s in SKILLS_TAXONOMY.get("soft_skills", []))
    soft_match_ratio = (len(resume_soft.intersection(jd_soft)) / max(1, len(jd_soft))) if jd_soft else 0.75

    # Overall Match Score (0 - 100)
    # Weighted: 55% hard skills, 30% semantic text, 15% soft skills
    raw_score = (hard_skill_ratio * 55) + (semantic_sim * 30) + (soft_match_ratio * 15)
    overall_match_score = int(np.clip(round(raw_score * 1.15), 15, 98))

    match_verdict = "Needs Significant Optimization"
    if overall_match_score >= 80:
        match_verdict = "Exceptional Match (High Interview Likelihood)"
    elif overall_match_score >= 65:
        match_verdict = "Strong Match (Competitive Candidate)"
    elif overall_match_score >= 50:
        match_verdict = "Moderate Match (Targeted Prep Needed)"

    return {
        "overall_match_score": overall_match_score,
        "match_verdict": match_verdict,
        "hard_skill_match_pct": round(min(100, hard_skill_ratio * 100)),
        "soft_skill_match_pct": round(min(100, soft_match_ratio * 100)),
        "semantic_similarity_pct": round(semantic_sim * 100),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "total_jd_skills_count": len(jd_skills),
        "total_matched_count": len(matched_skills)
    }

def categorize_missing_skills(missing_skills: List[str], target_role_key: str = None) -> List[Dict[str, Any]]:
    """
    Sorts missing skills into Priority Levels (High, Medium, Nice-to-Have)
    along with estimated learning time and difficulty.
    """
    categorized = []
    
    # Core skills for the target role if known
    core_role_skills = set()
    if target_role_key and target_role_key in CAREER_ROLES:
        core_role_skills = set(CAREER_ROLES[target_role_key].get("core_skills", []))

    for idx, skill in enumerate(missing_skills):
        is_core = skill in core_role_skills or idx < 3
        if is_core:
            priority = "High Priority"
            badge_color = "red"
            time_to_learn = "2-3 Weeks"
            difficulty = "Intermediate"
            why_needed = f"Critical requirement frequently assessed in technical screenings for this career path."
        elif idx < 7:
            priority = "Medium Priority"
            badge_color = "amber"
            time_to_learn = "1-2 Weeks"
            difficulty = "Beginner to Intermediate"
            why_needed = f"High-demand competency that gives you an edge over average applicants."
        else:
            priority = "Nice to Have"
            badge_color = "blue"
            time_to_learn = "3-5 Days"
            difficulty = "Beginner"
            why_needed = f"Differentiating skill for enterprise scale and team collaboration."

        categorized.append({
            "skill": skill,
            "priority": priority,
            "badge_color": badge_color,
            "time_to_learn": time_to_learn,
            "difficulty": difficulty,
            "why_needed": why_needed
        })

    return categorized

def recommend_job_roles(resume_text: str, resume_skills: List[str], user_interests: List[str]) -> List[Dict[str, Any]]:
    """
    Ranks suitable career roles from CAREER_ROLES based on skill overlap,
    resume text relevance, and candidate stated interests.
    """
    resume_skills_set = set(resume_skills)
    interests_lower = " ".join(user_interests).lower()
    recommendations = []

    for role_key, role_data in CAREER_ROLES.items():
        core_skills = set(role_data["core_skills"])
        secondary_skills = set(role_data.get("secondary_skills", []))
        
        # Overlap calculations
        core_overlap = len(resume_skills_set.intersection(core_skills))
        core_ratio = core_overlap / max(1, len(core_skills))
        
        sec_overlap = len(resume_skills_set.intersection(secondary_skills))
        sec_ratio = sec_overlap / max(1, len(secondary_skills))

        # Check interest alignment
        interest_boost = 0.0
        role_title_lower = role_data["title"].lower()
        role_cat_lower = role_data["category"].lower()
        for interest in user_interests:
            interest_clean = interest.lower()
            if interest_clean in role_title_lower or interest_clean in role_cat_lower:
                interest_boost += 0.15
            for kw in role_data.get("match_keywords", []):
                if kw in interest_clean:
                    interest_boost += 0.08
                    break
        interest_boost = min(0.25, interest_boost)

        # Keyword presence in resume text
        keyword_hits = 0
        for kw in role_data.get("match_keywords", []):
            if re.search(rf'\b{re.escape(kw)}\b', resume_text, re.IGNORECASE):
                keyword_hits += 1
        kw_ratio = keyword_hits / max(1, len(role_data.get("match_keywords", [])))

        # Composite role match score (0 - 100)
        fit_score = (core_ratio * 45) + (sec_ratio * 20) + (kw_ratio * 20) + (interest_boost * 100 * 0.15)
        # Normalization
        confidence = int(np.clip(round(fit_score * 1.25), 35, 96))

        # Determine matched and missing skills for this specific role
        matched_for_role = sorted(list(resume_skills_set.intersection(core_skills.union(secondary_skills))))
        missing_for_role = sorted(list(core_skills.difference(resume_skills_set)))

        recommendations.append({
            "role_key": role_key,
            "title": role_data["title"],
            "category": role_data["category"],
            "confidence": confidence,
            "salary_range": role_data["salary_range"],
            "market_demand": role_data["market_demand"],
            "demand_score": role_data["demand_score"],
            "description": role_data["description"],
            "why_it_fits": f"Matches {len(matched_for_role)} of your demonstrated skills including {', '.join(matched_for_role[:3]) or 'foundational programming'}.",
            "matched_skills": matched_for_role,
            "missing_skills": missing_for_role[:4],
            "project_templates": role_data.get("project_templates", []),
            "interview_questions": role_data.get("interview_questions", [])
        })

    # Sort descending by match confidence
    recommendations.sort(key=lambda x: x["confidence"], reverse=True)
    return recommendations

def calculate_career_readiness(
    match_score: int,
    impact_analysis: Dict[str, Any],
    resume_skills: List[str],
    has_projects: bool = True
) -> Dict[str, Any]:
    """
    Computes an overall Career Readiness Score (0-100) with diagnostic breakdown:
    - Technical Skill Competency (35%)
    - Resume Impact & ATS Quality (25%)
    - Project Portfolio Strength (20%)
    - Experience / Quantified Accomplishments (20%)
    """
    # 1. Technical Competency (0 - 100)
    skill_count = len(resume_skills)
    tech_score = min(95, max(40, skill_count * 5 + 30))

    # 2. Resume Impact & ATS Score (0 - 100)
    resume_ats_score = impact_analysis.get("impact_score", 65)

    # 3. Project Strength (0 - 100)
    project_score = 80 if has_projects else 50
    if impact_analysis.get("quantified_count", 0) >= 3:
        project_score = min(95, project_score + 15)

    # 4. Job Alignment (0 - 100)
    alignment_score = match_score

    # Weighted Overall Readiness Score
    overall_readiness = round(
        (tech_score * 0.35) +
        (resume_ats_score * 0.25) +
        (project_score * 0.20) +
        (alignment_score * 0.20)
    )
    overall_readiness = int(np.clip(overall_readiness, 25, 96))

    # Tier badge & diagnosis
    if overall_readiness >= 85:
        status_tier = "Interview Ready"
        color_class = "emerald"
        summary_advice = "Your profile is competitive for high-demand openings! Focus on mock interview drills and system design questions."
    elif overall_readiness >= 70:
        status_tier = "Competitive with Targeted Polish"
        color_class = "blue"
        summary_advice = "Strong technical foundation. Polishing 2-3 missing skills and adding 1 targeted portfolio project will place you in the top 10% of applicants."
    elif overall_readiness >= 50:
        status_tier = "Skill Builder Phase"
        color_class = "amber"
        summary_advice = "Good baseline! Follow the personalized 12-week roadmap to build production projects and master essential frameworks."
    else:
        status_tier = "Foundational Stage"
        color_class = "red"
        summary_advice = "Start with the recommended core languages and complete the step-by-step portfolio projects to establish your technical footprint."

    # Quick wins for fast improvement
    quick_wins = []
    if impact_analysis.get("quantified_count", 0) < 3:
        quick_wins.append("Add measurable outcomes to your projects (e.g. 'Reduced latency by 35%', 'Served 2,000+ users').")
    if impact_analysis.get("strong_verbs_count", 0) < 5:
        quick_wins.append("Replace passive phrases like 'worked on' with strong action verbs like 'Architected', 'Spearheaded', 'Optimized'.")
    if len(impact_analysis.get("weak_phrases", [])) > 0:
        quick_wins.append(f"Remove passive filler words ({', '.join(impact_analysis.get('weak_phrases', [])[:2])}) from experience bullets.")
    quick_wins.append("Include links to active GitHub repositories and live deployed project demos.")

    return {
        "overall_score": overall_readiness,
        "status_tier": status_tier,
        "color_class": color_class,
        "summary_advice": summary_advice,
        "breakdown": {
            "technical_competency": tech_score,
            "resume_impact_ats": resume_ats_score,
            "project_strength": project_score,
            "job_alignment": alignment_score
        },
        "quick_wins": quick_wins
    }

def generate_personalized_roadmap(top_role: Dict[str, Any], missing_skills: List[str]) -> List[Dict[str, Any]]:
    """
    Generates a personalized 4-phase learning roadmap incorporating candidate's missing skills.
    """
    role_key = top_role.get("role_key", "full_stack_developer")
    base_phases = CAREER_ROLES.get(role_key, CAREER_ROLES["full_stack_developer"]).get("roadmap_phases", [])
    
    custom_roadmap = []
    missing_iter = iter(missing_skills[:6])

    for i, phase in enumerate(base_phases):
        topics = list(phase["topics"])
        # Inject relevant missing skill into topics
        try:
            next_missing = next(missing_iter)
            topics.append(f"Mastery of {next_missing} & real-world integration")
        except StopIteration:
            pass

        # Curated resources
        resources = [
            {"name": "Official Docs & Tutorials", "type": "Documentation", "free": True},
            {"name": "freeCodeCamp / Roadmap.sh Guide", "type": "Interactive Guide", "free": True},
            {"name": "GitHub Awesome Curated List", "type": "Code Examples", "free": True}
        ]

        custom_roadmap.append({
            "phase": phase["phase"],
            "duration": phase["duration"],
            "topics": topics,
            "goal": phase["goal"],
            "resources": resources,
            "completed": False
        })

    return custom_roadmap
