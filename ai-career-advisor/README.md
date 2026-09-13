# AI Career Advisor & Resume Analyzer 🚀

An end-to-end intelligent career navigation and resume analysis application designed to help students, recent graduates, and job seekers answer three fundamental career questions:
> **1. Based on my resume, skills, and interests, which career roles are best for me?**  
> **2. What critical skills and qualifications am I currently missing?**  
> **3. How can I prepare through structured roadmaps, portfolio projects, and interview drills?**

---

## 🌟 Key Features & The 9 Core Modules

| Module | What It Delivers |
| :--- | :--- |
| **1. Resume Analysis** | Extracts contact info, word count, impact score, ATS formatting, and checks for strong action verbs vs. weak phrasing and quantifiable metrics (`%`, `$`, scale). |
| **2. Recommended Job Roles** | Ranks top career roles (Full Stack, Backend, Data Science, AI/ML, DevOps, Cybersecurity, etc.) based on skills, project keywords, and stated interests with market demand and salary benchmarks. |
| **3. Resume–Job Match %** | Visual match gauge comparing candidate resume against a target job description, featuring Hard Skill match %, Soft Skill match %, and ATS semantic keyword compatibility. |
| **4. Skill Analysis** | Categorizes extracted competencies into Programming Languages, Frameworks, Databases, Cloud & DevOps, Architecture, AI/Data, and Soft Skills. |
| **5. Missing Skills (Gap Analysis)** | Prioritized breakdown of missing competencies into **High Priority** (must-haves), **Medium Priority**, and **Nice-to-Have**, complete with difficulty and estimated learning time. |
| **6. Personalized Learning Roadmap** | Interactive 4-phase, 12-week preparation timeline tailored to close candidate skill gaps, with interactive completion checkboxes and curated free resources. |
| **7. Recommended Projects** | Tailored portfolio project ideas engineered to bridge missing skills, including architecture specs, tech stacks, and ready-to-use resume bullet points (Google XYZ formula). |
| **8. Interview Questions** | Role-specific technical questions, system design challenges, and behavioral (STAR method) scenarios with expandable model answer keys. |
| **9. Career Readiness Score** | Weighted composite score (0–100) combining Technical Competency, Resume/ATS Quality, Project Strength, and Job Alignment, backed by actionable "Quick Wins". |

---

## ⚡ Dual Engine Architecture

The application is built with a resilient dual-engine architecture:
1. **Built-in Semantic NLP Engine (100% Offline, Zero-Cost)**:
   - Uses `scikit-learn` TF-IDF vectorization, cosine similarity, regex pattern matchers, and a comprehensive 500+ skill taxonomy database.
   - Works immediately out of the box with zero external API keys or subscription requirements.
2. **Optional Generative AI Engine (Google Gemini)**:
   - Enter your Google Gemini API key in the UI settings or export `GEMINI_API_KEY` to unlock hyper-personalized executive summaries, AI-optimized resume bullet rewrites, and deep custom interview questions.
   - Automatically falls back to the NLP engine if no key is provided or if network limits are reached.

---

## 📁 Project Structure

```text
ai-career-advisor/
├── analyzer/
│   ├── __init__.py           # Master analysis pipeline
│   ├── parser.py             # PDF, DOCX, TXT text & metric extraction
│   ├── skills_db.py          # 500+ skills taxonomy and alias mappings
│   ├── roles_db.py           # 16+ career role definitions & interview banks
│   ├── nlp_engine.py         # TF-IDF, match scoring, readiness, roadmaps
│   ├── ai_engine.py          # Optional Google Gemini API integration
│   └── samples.py            # Built-in sample resumes, JDs, and interests
├── static/
│   ├── css/
│   │   └── custom.css        # Glassmorphism, animations, print styling
│   └── js/
│       └── app.js            # UI logic, Chart.js radar & gauges, tab state
├── templates/
│   ├── index.html            # Main interactive dashboard UI
│   └── report.html           # Standalone printable/PDF export report
├── uploads/                  # Temporary upload directory
├── requirements.txt          # Python dependencies
├── run.bat                   # Windows one-click start script
├── test_analyzer.py          # Automated test suite
└── README.md                 # Documentation
```

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.10+ installed
- Modern web browser (Chrome, Edge, Firefox, Safari)

### 1. Install Dependencies
```bash
cd ai-career-advisor
pip install -r requirements.txt
```

### 2. Run the Application
On Windows, you can double-click `run.bat` or run:
```bash
python app.py
```

### 3. Open in Browser
Visit **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser.

---

## 🧪 Running Automated Tests

Run the test suite to verify all 9 modules and REST endpoints:
```bash
python test_analyzer.py
```

---

## 📄 Exporting Reports

Click **"Download / Print Report"** in the results header to open a clean, print-optimized document ready for saving as a PDF or printing hard copies for career counseling sessions.
