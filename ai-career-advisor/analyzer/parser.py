"""
Resume Parser Module.
Extracts raw text, contact information, sections, action verbs, and quantifiable impact metrics
from PDF, DOCX, and plain text files.
"""

import re
import io
from typing import Dict, Any, List, Optional
import pypdf
import docx

# Action verbs commonly looked for in high-impact technical resumes
STRONG_ACTION_VERBS = [
    "architected", "engineered", "developed", "spearheaded", "optimized", "implemented",
    "designed", "deployed", "scaled", "automated", "orchestrated", "refactored",
    "reduced", "increased", "boosted", "accelerated", "integrated", "built",
    "constructed", "mentored", "led", "streamlined", "delivered", "championed",
    "overhauled", "migrated", "configured", "launched", "standardized", "audited"
]

WEAK_ACTION_VERBS = [
    "worked on", "helped with", "assisted", "responsible for", "participated in",
    "familiar with", "handled", "did", "was involved in", "duties included"
]

def extract_text_from_stream(stream_bytes: bytes, filename: str) -> str:
    """Extract clean UTF-8 text from file bytes based on filename extension."""
    filename_lower = filename.lower()
    
    if filename_lower.endswith(".pdf"):
        reader = pypdf.PdfReader(io.BytesIO(stream_bytes))
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        return clean_text(text)
        
    elif filename_lower.endswith(".docx"):
        doc = docx.Document(io.BytesIO(stream_bytes))
        text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
        # Also inspect tables if any
        for table in doc.tables:
            for row in table.rows:
                row_text = " | ".join([cell.text.strip() for cell in row.cells if cell.text.strip()])
                if row_text:
                    text += "\n" + row_text
        return clean_text(text)
        
    else:
        # Fallback to UTF-8 / latin-1 text
        try:
            return clean_text(stream_bytes.decode("utf-8"))
        except UnicodeDecodeError:
            return clean_text(stream_bytes.decode("latin-1", errors="ignore"))

def clean_text(text: str) -> str:
    """Normalize whitespace and remove non-printable characters."""
    if not text:
        return ""
    # Normalize bullet points and line breaks
    text = re.sub(r'[\r\t]', ' ', text)
    text = re.sub(r'[\u2022\u2023\u25E6\u2043\u2219\u00B7]', ' * ', text)
    # Remove excessive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Normalize spaces
    text = re.sub(r'[ ]{2,}', ' ', text)
    return text.strip()

def extract_contact_info(text: str) -> Dict[str, Optional[str]]:
    """Extract email, phone, github, linkedin, and website links."""
    # Email regex
    email_match = re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
    email = email_match.group(0) if email_match else None

    # Phone regex (international & US formats)
    phone_match = re.search(r'(\+?\d{1,3}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}', text)
    phone = phone_match.group(0) if phone_match else None

    # LinkedIn
    linkedin_match = re.search(r'(?:https?://)?(?:www\.)?linkedin\.com/in/[a-zA-Z0-9_-]+', text, re.IGNORECASE)
    linkedin = linkedin_match.group(0) if linkedin_match else None

    # GitHub
    github_match = re.search(r'(?:https?://)?(?:www\.)?github\.com/[a-zA-Z0-9_-]+', text, re.IGNORECASE)
    github = github_match.group(0) if github_match else None

    # Portfolio / general website
    portfolio_match = re.search(r'(?:https?://)?([a-zA-Z0-9-]+\.(?:dev|me|io|tech|app|com|org|net)(?:/[^\s]*)?)', text, re.IGNORECASE)
    portfolio = None
    if portfolio_match:
        url = portfolio_match.group(0)
        if "linkedin.com" not in url.lower() and "github.com" not in url.lower():
            portfolio = url

    # Candidate name heuristic: first non-empty line if it has 2-4 words and no symbols
    name = None
    for line in text.splitlines():
        line = line.strip()
        if not line or "@" in line or "http" in line or len(line) > 50:
            continue
        words = line.split()
        if 2 <= len(words) <= 4 and all(w.isalpha() for w in words):
            name = line
            break

    return {
        "name": name or "Candidate",
        "email": email,
        "phone": phone,
        "linkedin": linkedin,
        "github": github,
        "portfolio": portfolio
    }

def extract_sections(text: str) -> Dict[str, str]:
    """Identify standard resume sections (Education, Experience, Projects, Skills, Summary)."""
    section_keywords = {
        "summary": ["summary", "profile", "objective", "about me", "professional summary"],
        "experience": ["experience", "work history", "employment", "work experience", "internships", "professional experience"],
        "education": ["education", "academic background", "academics", "qualifications"],
        "projects": ["projects", "personal projects", "academic projects", "key projects"],
        "skills": ["skills", "technical skills", "core competencies", "technologies", "tech stack"],
        "certifications": ["certifications", "licenses", "courses", "certificates"]
    }

    lines = text.splitlines()
    detected_sections: Dict[str, List[str]] = {k: [] for k in section_keywords}
    current_sec = "summary"

    for line in lines:
        line_clean = line.strip().lower()
        if not line_clean:
            continue
            
        matched_new_section = False
        # Check if line looks like a header (short, capitalized or standalone)
        if len(line_clean) < 35:
            for sec_key, keywords in section_keywords.items():
                if any(re.match(rf'^{kw}[:\s]*$', line_clean) for kw in keywords):
                    current_sec = sec_key
                    matched_new_section = True
                    break
        
        if not matched_new_section:
            detected_sections[current_sec].append(line)

    return {k: "\n".join(v).strip() for k, v in detected_sections.items() if v}

def analyze_resume_metrics_and_impact(text: str) -> Dict[str, Any]:
    """
    Analyzes resume text for measurable impacts, action verbs,
    weak phrases, word count, and structure.
    """
    text_lower = text.lower()
    words = re.findall(r'\b[a-zA-Z]+\b', text_lower)
    total_word_count = len(words)
    
    # 1. Detect strong action verbs
    found_strong_verbs = []
    for verb in STRONG_ACTION_VERBS:
        if re.search(rf'\b{verb}\b', text_lower):
            found_strong_verbs.append(verb.capitalize())
            
    # 2. Detect weak/passive phrases
    found_weak_phrases = []
    for phrase in WEAK_ACTION_VERBS:
        if phrase in text_lower:
            found_weak_phrases.append(phrase)

    # 3. Detect quantifiable metrics (%, $, numbers like 10x, 40%, 100k)
    metrics_patterns = [
        r'\b\d+(?:\.\d+)?%',                      # Percentages: 45%, 99.9%
        r'\$\s?\d+(?:,\d{3})*(?:\.\d+)?[kmb]?',    # Currency: $100k, $1.2M
        r'\b\d+x\b',                               # Multipliers: 10x, 2x
        r'\b\d+(?:,\d{3})+\b',                     # Large counts: 10,000, 50,000
        r'\breduced by \d+',                       # Metric phrases
        r'\bincreased by \d+',
        r'\bimproved by \d+'
    ]
    quantified_matches = []
    for p in metrics_patterns:
        matches = re.findall(p, text, re.IGNORECASE)
        quantified_matches.extend(matches)
        
    quantified_count = len(quantified_matches)
    
    # Impact score out of 100
    # Factors: strong verbs count (max 40 pts), quantified metrics (max 40 pts), absence of weak phrases (20 pts)
    verb_score = min(40, len(found_strong_verbs) * 4)
    metric_score = min(40, quantified_count * 8)
    weakness_penalty = min(20, len(found_weak_phrases) * 5)
    impact_score = max(20, min(98, (verb_score + metric_score + (20 - weakness_penalty))))

    # Readability / Length analysis
    word_count_status = "Optimal"
    if total_word_count < 200:
        word_count_status = "Too Short (Under 200 words)"
    elif total_word_count > 1000:
        word_count_status = "Slightly Long (Over 1,000 words)"
        
    return {
        "total_words": total_word_count,
        "word_count_status": word_count_status,
        "strong_action_verbs": found_strong_verbs[:10],
        "strong_verbs_count": len(found_strong_verbs),
        "weak_phrases": found_weak_phrases,
        "quantified_metrics": list(set(quantified_matches))[:8],
        "quantified_count": quantified_count,
        "impact_score": round(impact_score),
    }
