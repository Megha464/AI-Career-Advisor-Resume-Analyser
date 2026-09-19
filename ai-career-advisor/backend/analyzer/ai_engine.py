"""
AI Generative Engine Integration (Gemini / LLM).
Provides optional deep LLM analysis when an API key is provided,
with seamless fallback to the local offline NLP engine.
"""

import os
import json
import requests
from typing import Dict, Any, Optional

def generate_ai_enhanced_advisory(
    resume_text: str,
    target_jd: str,
    user_interests: list,
    base_analysis: Dict[str, Any],
    api_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    If api_key is available (or set in GEMINI_API_KEY env var), calls Gemini API
    to enrich resume summary, bullet point improvements, tailored interview questions,
    and hyper-specific project ideas.
    """
    effective_key = api_key or os.getenv("GEMINI_API_KEY", "").strip()
    if not effective_key:
        return base_analysis

    prompt = f"""
You are an expert AI Career Advisor and Technical Recruiter.
Analyze the following candidate's resume against their stated interests and target job description.

Candidate Resume Excerpt:
\"\"\"{resume_text[:2500]}\"\"\"

Target Job Description:
\"\"\"{target_jd[:1500] if target_jd else "Software Engineering / Tech Role based on skills"}\"\"\"

Candidate Stated Interests:
{', '.join(user_interests) if user_interests else "General Software Development"}

Current Detected Base Analysis:
- Readiness Score: {base_analysis.get('readiness_score', {}).get('overall_score')}
- Top Role: {base_analysis.get('recommended_roles', [{}])[0].get('title', 'Software Engineer')}
- Missing Skills: {', '.join([s['skill'] for s in base_analysis.get('missing_skills', [])[:5]])}

Please provide an enhanced JSON response adhering STRICTLY to this JSON format:
{{
  "ai_powered": true,
  "executive_summary": "A 2-3 sentence executive recruiter summary of the candidate's core strengths and trajectory.",
  "top_strengths": ["Strength 1 with context", "Strength 2 with context", "Strength 3 with context"],
  "critical_weaknesses": ["Weakness 1 to fix", "Weakness 2 to fix"],
  "tailored_interview_questions": [
    {{
      "category": "Technical",
      "question": "Specific question testing one of their claimed skills",
      "what_interviewers_look_for": "Specific technical insight",
      "sample_answer_framework": "STAR / concept outline"
    }},
    {{
      "category": "System Design",
      "question": "Real-world engineering challenge relevant to their target role",
      "what_interviewers_look_for": "Trade-offs and architectural decisions",
      "sample_answer_framework": "Components, bottlenecks, scalability"
    }},
    {{
      "category": "Behavioral",
      "question": "Behavioral question targeting leadership/teamwork",
      "what_interviewers_look_for": "Ownership and conflict resolution",
      "sample_answer_framework": "Situation, Task, Action, Result"
    }}
  ],
  "improved_resume_bullets": [
    {{
      "original_concept": "Generic responsibility",
      "optimized_bullet": "Accomplished [X], as measured by [Y], by doing [Z]"
    }},
    {{
      "original_concept": "Generic responsibility",
      "optimized_bullet": "Accomplished [X], as measured by [Y], by doing [Z]"
    }}
  ]
}}
Only return valid JSON. Do not include markdown code block syntax if possible, or use standard json formatting.
"""

    headers = {"Content-Type": "application/json"}
    # Use Gemini 2.5 Flash / 1.5 Flash
    models_to_try = ["gemini-2.5-flash", "gemini-1.5-flash"]

    for model in models_to_try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={effective_key}"
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "temperature": 0.2,
                "response_mime_type": "application/json"
            }
        }
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=12)
            if resp.status_code == 200:
                data = resp.json()
                content = data["candidates"][0]["content"]["parts"][0]["text"]
                # Clean markdown backticks if returned
                content = content.strip()
                if content.startswith("```json"):
                    content = content[7:]
                if content.startswith("```"):
                    content = content[3:]
                if content.endswith("```"):
                    content = content[:-3]
                    
                parsed_llm = json.loads(content.strip())
                
                # Merge into base analysis seamlessly
                enhanced = dict(base_analysis)
                enhanced["ai_powered"] = True
                enhanced["executive_summary"] = parsed_llm.get("executive_summary", enhanced.get("executive_summary"))
                if parsed_llm.get("top_strengths"):
                    enhanced["resume_analysis"]["strengths"] = parsed_llm["top_strengths"]
                if parsed_llm.get("critical_weaknesses"):
                    enhanced["resume_analysis"]["weaknesses"] = parsed_llm["critical_weaknesses"]
                if parsed_llm.get("tailored_interview_questions"):
                    enhanced["interview_questions"] = parsed_llm["tailored_interview_questions"]
                if parsed_llm.get("improved_resume_bullets"):
                    enhanced["improved_resume_bullets"] = parsed_llm["improved_resume_bullets"]
                    
                return enhanced
        except Exception:
            continue

    # Fallback gracefully to base analysis
    return base_analysis
