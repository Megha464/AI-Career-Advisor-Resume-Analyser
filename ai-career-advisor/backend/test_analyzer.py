"""
Comprehensive Automated Test Suite for AI Career Advisor & Resume Analyzer.
Verifies all 9 output modules, parser, NLP semantic engine, and API routes.
"""

import os
import sys
import unittest
import json

# Ensure backend directory is in sys.path
backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app import app
from analyzer import run_complete_career_analysis
from analyzer.samples import SAMPLE_RESUMES, SAMPLE_JOB_DESCRIPTIONS

class TestCareerAdvisor(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.sample_resume = SAMPLE_RESUMES["junior_fullstack"]["text"]
        self.sample_jd = SAMPLE_JOB_DESCRIPTIONS["senior_fullstack"]["text"]
        self.sample_interests = ["Full-Stack Web Development", "Cloud Computing & DevOps"]

    def test_complete_analysis_pipeline(self):
        """Verify the 9 core modules in complete analysis pipeline."""
        result = run_complete_career_analysis(
            resume_text=self.sample_resume,
            target_jd=self.sample_jd,
            user_interests=self.sample_interests
        )

        # 1. Resume analysis
        self.assertIn("resume_analysis", result)
        self.assertIn("strengths", result["resume_analysis"])
        self.assertIn("weaknesses", result["resume_analysis"])
        self.assertIn("impact_metrics", result["resume_analysis"])
        self.assertGreater(result["resume_analysis"]["impact_metrics"]["impact_score"], 0)

        # 2. Recommended job roles
        self.assertIn("recommended_roles", result)
        self.assertGreater(len(result["recommended_roles"]), 0)
        top_role = result["recommended_roles"][0]
        self.assertIn("title", top_role)
        self.assertIn("confidence", top_role)
        self.assertIn("salary_range", top_role)

        # 3. Resume-Job match percentage
        self.assertIn("match_analysis", result)
        self.assertIn("overall_match_score", result["match_analysis"])
        self.assertGreaterEqual(result["match_analysis"]["overall_match_score"], 0)
        self.assertLessEqual(result["match_analysis"]["overall_match_score"], 100)

        # 4. Skill analysis
        self.assertIn("skill_analysis", result)
        self.assertIn("by_category", result["skill_analysis"])
        self.assertGreater(result["skill_analysis"]["total_skills_count"], 0)

        # 5. Missing skills
        self.assertIn("missing_skills", result)
        self.assertIsInstance(result["missing_skills"], list)

        # 6. Personalized learning roadmap
        self.assertIn("learning_roadmap", result)
        self.assertGreater(len(result["learning_roadmap"]), 0)

        # 7. Recommended projects
        self.assertIn("recommended_projects", result)
        self.assertGreater(len(result["recommended_projects"]), 0)
        self.assertIn("resume_bullet", result["recommended_projects"][0])

        # 8. Interview questions
        self.assertIn("interview_questions", result)
        self.assertGreater(len(result["interview_questions"]), 0)

        # 9. Career readiness score
        self.assertIn("readiness_score", result)
        self.assertIn("overall_score", result["readiness_score"])
        self.assertIn("breakdown", result["readiness_score"])
        self.assertIn("quick_wins", result["readiness_score"])

    def test_samples_api_endpoint(self):
        """Verify /api/samples returns resumes, JDs, and interests."""
        response = self.app.get('/api/samples')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("resumes", data)
        self.assertIn("job_descriptions", data)
        self.assertIn("interests", data)

    def test_analyze_api_endpoint(self):
        """Verify /api/analyze handles POST request and returns valid JSON."""
        payload = {
            "resume_text": self.sample_resume,
            "target_jd": self.sample_jd,
            "interests": self.sample_interests
        }
        response = self.app.post(
            '/api/analyze',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        res_json = response.get_json()
        self.assertTrue(res_json["success"])
        self.assertIn("data", res_json)

    def test_export_report_endpoint(self):
        """Verify /api/export-report renders printable HTML view."""
        result = run_complete_career_analysis(
            resume_text=self.sample_resume,
            target_jd=self.sample_jd,
            user_interests=self.sample_interests
        )
        response = self.app.post(
            '/api/export-report',
            data=json.dumps(result),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Career Advisory", response.data)

    def test_frontend_serving(self):
        """Verify frontend templates and static assets are located and served correctly."""
        # Index template
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"AI Career Advisor & Resume Analyzer", response.data)

        # Static CSS
        response = self.app.get('/static/css/custom.css')
        self.assertEqual(response.status_code, 200)

        # Static JS
        response = self.app.get('/static/js/app.js')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
