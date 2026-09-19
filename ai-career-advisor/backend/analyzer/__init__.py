"""
AI Career Advisor & Resume Analyzer Core Module
Integrates Parser, NLP Semantic Matching, Role Recommendations,
Gap Analysis, Roadmap Generation, Projects, Interview Prep, and LLM Enhancements.
"""

from typing import Dict, Any, List, Optional

from .parser import (
    extract_text_from_stream,
    extract_contact_info,
    extract_sections,
    analyze_resume_metrics_and_impact
)
from .nlp_engine import (
    extract_skills_from_text,
    calculate_resume_job_match,
    categorize_missing_skills,
    recommend_job_roles,
    calculate_career_readiness,
    generate_personalized_roadmap
)
from .ai_engine import generate_ai_enhanced_advisory
from .roles_db import CAREER_ROLES

def run_complete_career_analysis(
    resume_text: str,
    target_jd: str = "",
    user_interests: Optional[List[str]] = None,
    api_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Executes end-to-end Career Advisory and Resume Analysis pipeline:
    1. Resume Analysis (Summary, Strengths, Weaknesses, Impact metrics, Contact info)
    2. Recommended Job Roles
    3. Resume–Job Match Percentage
    4. Skill Analysis (Categorized technical & soft skills)
    5. Missing Skills (Prioritized gap analysis)
    6. Personalized Learning Roadmap (4 Phases with actionable milestones)
    7. Recommended Projects (Tailored portfolio ideas with tech stack & resume bullets)
    8. Interview Questions (Technical, Behavioral, System Design)
    9. Career Readiness Score (Weighted composite score with quick wins)
    """
    if user_interests is None:
        user_interests = []

    # 1. Parse Resume Metadata & Impact Metrics
    contact_info = extract_contact_info(resume_text)
    sections = extract_sections(resume_text)
    impact_analysis = analyze_resume_metrics_and_impact(resume_text)

    # 2. Extract Skills from Resume
    skills_data = extract_skills_from_text(resume_text)
    resume_skills = skills_data["all_skills"]
    categorized_skills = skills_data["by_category"]

    # 3. Recommend Job Roles based on skills and interests
    recommended_roles = recommend_job_roles(resume_text, resume_skills, user_interests)
    top_role = recommended_roles[0] if recommended_roles else None

    # If target JD is empty, construct a default JD from the top recommended role
    effective_jd = target_jd.strip()
    if not effective_jd and top_role:
        role_key = top_role.get("role_key", "full_stack_developer")
        role_def = CAREER_ROLES.get(role_key, CAREER_ROLES["full_stack_developer"])
        effective_jd = f"Target Role: {role_def['title']}\n\nRequired Skills: {', '.join(role_def['core_skills'])}\n\nPreferred Skills: {', '.join(role_def.get('secondary_skills', []))}\n\nDescription: {role_def['description']}"

    # 4. Resume-Job Match Analysis
    match_analysis = calculate_resume_job_match(resume_text, resume_skills, effective_jd)

    # 5. Missing Skills Analysis
    raw_missing_skills = match_analysis["missing_skills"]
    # If missing skills is empty, supply top secondary skills from top role
    if not raw_missing_skills and top_role:
        raw_missing_skills = top_role.get("missing_skills", ["Cloud Architecture", "Docker", "CI/CD"])
        
    categorized_missing = categorize_missing_skills(
        raw_missing_skills,
        target_role_key=top_role.get("role_key") if top_role else None
    )

    # 6. Career Readiness Score
    has_projects_section = "projects" in sections or "project" in resume_text.lower()
    readiness_data = calculate_career_readiness(
        match_score=match_analysis["overall_match_score"],
        impact_analysis=impact_analysis,
        resume_skills=resume_skills,
        has_projects=has_projects_section
    )

    # 7. Personalized Learning Roadmap
    roadmap = generate_personalized_roadmap(top_role, raw_missing_skills)

    # 8. Recommended Projects (Tailored from top role or missing skills)
    recommended_projects = []
    if top_role and top_role.get("project_templates"):
        recommended_projects = top_role["project_templates"]
    else:
        # Fallback default project
        recommended_projects = [{
            "title": "Cloud-Native Microservices Application",
            "summary": "Full-stack cloud-native app designed to bridge detected technical skill gaps.",
            "tech_stack": raw_missing_skills[:4] + ["PostgreSQL", "Docker"],
            "key_features": ["Secure RESTful endpoints", "Automated unit tests", "Containerized deployment"],
            "resume_bullet": f"Engineered a scalable full-stack application using {', '.join(raw_missing_skills[:3])}, serving 500+ daily active users."
        }]

    # 9. Interview Questions
    interview_questions = []
    if top_role and top_role.get("interview_questions"):
        interview_questions = top_role["interview_questions"]
    else:
        interview_questions = [
            {
                "category": "Technical",
                "question": f"How do you handle error handling, logging, and concurrency in production?",
                "key_points": ["Structured logging", "Graceful degradation", "Async patterns"]
            }
        ]

    # Executive Resume Strengths & Weaknesses
    strengths = []
    if len(resume_skills) >= 8:
        strengths.append(f"Diverse technical skill set spanning {len(resume_skills)} core industry technologies.")
    if impact_analysis["quantified_count"] >= 2:
        strengths.append(f"Demonstrated quantifiable achievements ({impact_analysis['quantified_count']} metrics found).")
    if impact_analysis["strong_verbs_count"] >= 5:
        strengths.append(f"Effective use of proactive engineering action verbs ({', '.join(impact_analysis['strong_action_verbs'][:3])}).")
    if not strengths:
        strengths.append("Clear foundational technical aptitude and structured project experience.")

    weaknesses = []
    if impact_analysis["quantified_count"] < 2:
        weaknesses.append("Lack of quantifiable business metrics (% improvements, latency reductions, user scale) in project bullets.")
    if len(categorized_missing) > 0:
        weaknesses.append(f"Missing key requirements for target roles, notably: {', '.join([m['skill'] for m in categorized_missing[:3]])}.")
    if len(impact_analysis["weak_phrases"]) > 0:
        weaknesses.append(f"Contains passive phrasing ({', '.join(impact_analysis['weak_phrases'][:2])}) instead of direct ownership verbs.")
    if not weaknesses:
        weaknesses.append("Consider adding links to live deployed demo URLs and GitHub project repositories.")

    base_analysis = {
        "candidate_info": contact_info,
        "resume_analysis": {
            "summary": f"Candidate profile possessing solid competencies in {', '.join(resume_skills[:4]) if resume_skills else 'programming'} with career readiness score of {readiness_data['overall_score']}/100.",
            "strengths": strengths,
            "weaknesses": weaknesses,
            "impact_metrics": impact_analysis,
            "detected_sections": list(sections.keys())
        },
        "recommended_roles": recommended_roles[:4],
        "top_role": top_role,
        "match_analysis": match_analysis,
        "skill_analysis": {
            "total_skills_count": len(resume_skills),
            "by_category": categorized_skills,
            "all_skills": resume_skills
        },
        "missing_skills": categorized_missing,
        "learning_roadmap": roadmap,
        "recommended_projects": recommended_projects,
        "interview_questions": interview_questions,
        "readiness_score": readiness_data,
        "user_interests": user_interests,
        "target_jd_provided": bool(target_jd.strip()),
        "ai_powered": False
    }

    # Optional AI enhancement if API key is provided
    final_analysis = generate_ai_enhanced_advisory(
        resume_text=resume_text,
        target_jd=effective_jd,
        user_interests=user_interests,
        base_analysis=base_analysis,
        api_key=api_key
    )

    return final_analysis
