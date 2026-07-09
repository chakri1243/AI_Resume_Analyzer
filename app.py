from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import send_file

import os
from datetime import datetime

from database import db
from models import User, ResumeReport
from parser import extract_text
from section_extractor import analyze_resume
from ats_engine import calculate_ats
from jd_matcher import calculate_match
from pdf_report import create_report
from recommendations import get_missing_skills
from resume_recommendations import (
    generate_recommendations,
    predicted_score
)


from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

app = Flask(__name__)

# ======================
# Configuration
# ======================

app.config['SECRET_KEY'] = 'resume_analyzer_secret'

import os

database_url = os.environ.get("DATABASE_URL")

if database_url:
    database_url = database_url.replace(
        "postgres://",
        "postgresql://",
        1
    )

app.config['SQLALCHEMY_DATABASE_URI'] = (
    database_url or "sqlite:///resume.db"
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['REPORT_FOLDER'] = REPORT_FOLDER

# Create folders automatically
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

# Create database tables
with app.app_context():
    db.create_all()


# ======================
# Home Page
# ======================

@app.route('/')
def home():
    return render_template('index.html')


# ======================
# Register
# ======================

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(
            email=email
        ).first()

        if user:
            return "Email already exists."

        hashed_password = generate_password_hash(
            password
        )

        new_user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect('/login')

    return render_template(
        'register.html'
    )


# ======================
# Login
# ======================

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(
            email=email
        ).first()

        if user and check_password_hash(
                user.password,
                password):

            session['user_id'] = user.id
            session['user_name'] = user.name

            return redirect('/dashboard')

        return "Invalid Email or Password"

    return render_template(
        'login.html'
    )


# ======================
# Dashboard
# ======================

@app.route('/dashboard')
def dashboard():

    if 'user_id' not in session:
        return redirect('/login')

    return render_template(
        'dashboard.html',
        name=session['user_name']
    )


# ======================
# Upload Resume
# ======================

@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':

        file = request.files['resume']

        if file.filename == '':
            return "Please upload a file."

        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'],
            file.filename
        )

        file.save(filepath)

        # Extract resume text
        text = extract_text(filepath)

        # Analyze resume sections
        result = analyze_resume(text)

        # Calculate ATS Score
        ats = calculate_ats(
            result,
            text
        )

        result['ats_score'] = ats['ats_score']
        result['breakdown'] = ats['breakdown']
        result['suggestions'] = ats['suggestions']
        result['resume_tips'] = (
            generate_recommendations(
                result,
                text
            )
        )
        result['predicted_score'] = (
            predicted_score(
                result
            )
        )
    

    


        

        # ======================
        # Job Description Match
        # ======================

        jd = request.form.get(
            'job_description'
        )

        role = request.form.get(
            'job_role'
        )

        match_score = 0

        if jd and jd.strip() != "":
            match_score = calculate_match(
                text,
                jd
            )

        result['match_score'] = match_score

        # ======================
        # Missing Skills
        # ======================

        if role and role.strip() != "":
            result['missing_skills'] = (
                get_missing_skills(
                    result['skills'],
                    role
                )
            )
        else:
            result['missing_skills'] = []

        # ======================
        # Save Report History
        # ======================

        report = ResumeReport(
            user_id=session['user_id'],
            filename=file.filename,
            ats_score=result['ats_score'],
            match_score=match_score,
            date=str(
                datetime.now()
            )
        )

        db.session.add(report)
        db.session.commit()

        return render_template(
            'result.html',
            result=result
        )

    return render_template(
        'upload.html'
    )


# ======================
# Resume History
# ======================

@app.route('/history')
def history():

    if 'user_id' not in session:
        return redirect('/login')

    reports = ResumeReport.query.filter_by(
        user_id=session['user_id']
    ).all()

    return render_template(
        'history.html',
        reports=reports
    )


# ======================
# Download PDF Report
# ======================

@app.route('/download/<int:score>')
def download(score):

    filename = os.path.join(
        app.config['REPORT_FOLDER'],
        'ATS_Report.pdf'
    )

    create_report(
        score,
        filename
    )

    return send_file(
        filename,
        as_attachment=True
    )


# ======================
# Logout
# ======================

@app.route('/logout')
def logout():

    session.clear()

    return redirect('/')


# ======================
# Run Project
# ======================

if __name__ == '__main__':
    app.run(
        debug=True
    )