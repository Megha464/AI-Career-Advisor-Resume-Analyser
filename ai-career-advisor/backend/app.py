"""
AI Career Advisor & Resume Analyzer - Flask Web Application
Main entry point serving the UI dashboard and REST API.
"""

import os
import json
from flask import Flask, render_template, request, jsonify, make_response
from werkzeug.utils import secure_filename

from analyzer import (
    run_complete_career_analysis,
    extract_text_from_stream
)
from analyzer.samples import (
    SAMPLE_RESUMES,
    SAMPLE_JOB_DESCRIPTIONS,
    INTEREST_OPTIONS
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'frontend'))
TEMPLATE_DIR = os.path.join(FRONTEND_DIR, 'templates')
STATIC_DIR = os.path.join(FRONTEND_DIR, 'static')
UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')

app = Flask(
    __name__,
    template_folder=TEMPLATE_DIR,
    static_folder=STATIC_DIR
)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload
app.config['UPLOAD_FOLDER'] = UPLOAD_DIR
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Add CORS headers to enable standalone frontend development
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    return response

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt', 'md'}

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Render the interactive Career Advisor dashboard."""
    return render_template('index.html', interest_options=INTEREST_OPTIONS)

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "ai-career-advisor"})

@app.route('/api/samples', methods=['GET'])
def get_samples():
    """Return pre-configured sample resumes, job descriptions, and interests."""
    return jsonify({
        "resumes": SAMPLE_RESUMES,
        "job_descriptions": SAMPLE_JOB_DESCRIPTIONS,
        "interests": INTEREST_OPTIONS
    })

@app.route('/api/analyze', methods=['POST', 'OPTIONS'])
def analyze():
    if request.method == 'OPTIONS':
        return make_response(jsonify({"status": "ok"}), 200)
    """
    Main analysis endpoint. Accepts resume file upload OR pasted text,
    target job description, selected career interests, and optional API key.
    """
    try:
        resume_text = ""
        
        # 1. Check for file upload
        if 'resume_file' in request.files:
            file = request.files['resume_file']
            if file and file.filename and allowed_file(file.filename):
                stream_bytes = file.read()
                resume_text = extract_text_from_stream(stream_bytes, file.filename)
                
        # 2. Fallback to pasted text
        if not resume_text.strip():
            resume_text = request.form.get('resume_text', '').strip()

        # If JSON payload was posted instead of form-data
        if not resume_text and request.is_json:
            data = request.get_json()
            resume_text = data.get('resume_text', '').strip()
            target_jd = data.get('target_jd', '').strip()
            interests = data.get('interests', [])
            api_key = data.get('api_key', '').strip()
        else:
            target_jd = request.form.get('target_jd', '').strip()
            interests_raw = request.form.get('interests', '[]')
            try:
                interests = json.loads(interests_raw) if isinstance(interests_raw, str) else interests_raw
            except Exception:
                interests = [i.strip() for i in interests_raw.split(',') if i.strip()]
            api_key = request.form.get('api_key', '').strip()

        if not resume_text:
            return jsonify({
                "success": False,
                "error": "Please upload a resume file (.pdf, .docx, .txt) or paste your resume text."
            }), 400

        # Execute full analysis
        results = run_complete_career_analysis(
            resume_text=resume_text,
            target_jd=target_jd,
            user_interests=interests,
            api_key=api_key
        )

        return jsonify({
            "success": True,
            "data": results
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            "success": False,
            "error": f"Analysis failed: {str(e)}"
        }), 500

@app.route('/api/export-report', methods=['POST', 'OPTIONS'])
def export_report():
    if request.method == 'OPTIONS':
        return make_response('', 200)
    """Render a standalone, print-friendly complete report."""
    try:
        report_data = request.get_json()
        if not report_data:
            return "Invalid report data", 400
        return render_template('report.html', data=report_data)
    except Exception as e:
        return f"Error generating report: {str(e)}", 500

if __name__ == '__main__':
    import sys
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    port = int(os.environ.get("PORT", 5000))
    print(f"[INFO] AI Career Advisor & Resume Analyzer running at: http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=False)
