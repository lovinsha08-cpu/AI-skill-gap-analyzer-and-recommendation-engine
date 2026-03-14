from flask import Flask, request, render_template, redirect, url_for, session
import pickle
from PyPDF2 import PdfReader
import re
import os
from skills_reference import skills_reference
from difflib import SequenceMatcher
import sys

# -----------------------------
# Import your quiz questions properly
# -----------------------------
sys.path.append(r"C:\Users\lovin\OneDrive\Documents\skillgap_analyzer")  # folder path
from quiz_questions import quiz_questions  # your variable inside the file

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # required for session tracking in quiz

# -----------------------------
# Load models
# -----------------------------
if not os.path.exists("models"):
    raise FileNotFoundError("Models folder not found. Run train_model.py first.")

rf_classifier = pickle.load(open('models/rf_classifier_categorization.pkl', 'rb'))
tfidf_vectorizer = pickle.load(open('models/tfidf_vectorizer_categorization.pkl', 'rb'))

# -----------------------------
# PDF to text
# -----------------------------
def pdf_to_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "
    return text

# -----------------------------
# Text cleaning
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

# -----------------------------
# Fuzzy skill matching
# -----------------------------
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def extract_skills(text, skill_list, threshold=0.6):
    text = clean_text(text)
    found = []
    for skill in skill_list:
        skill_clean = skill.lower()
        if skill_clean in text:
            found.append(skill)
        else:
            skill_words = skill_clean.split()
            for word in skill_words:
                for t_word in text.split():
                    if similar(word, t_word) >= threshold:
                        found.append(skill)
                        break
                else:
                    continue
                break
    if len(found) < 3:
        found += skill_list[:3]
        found = list(set(found))
    return found

# -----------------------------
# Skill gap analysis
# -----------------------------
def skill_gap_analysis(category, resume_text):
    if category not in skills_reference:
        category = list(skills_reference.keys())[0]
    expected_skills = skills_reference.get(category, [])
    candidate_skills = extract_skills(resume_text, expected_skills)
    missing_skills = list(set(expected_skills) - set(candidate_skills))
    return expected_skills, candidate_skills, missing_skills

# -----------------------------
# Home page (resume upload)
# -----------------------------
@app.route("/")
def home():
    return render_template("resume.html")

# -----------------------------
# Resume prediction
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    if "resume" not in request.files:
        return render_template("resume.html", error="No file uploaded")

    file = request.files["resume"]
    if file.filename == "":
        return render_template("resume.html", error="Please upload a file")

    text = pdf_to_text(file)
    if text.strip() == "":
        return render_template("resume.html", error="Could not read PDF")

    vector = tfidf_vectorizer.transform([text])
    prediction = rf_classifier.predict(vector)[0]
    expected, found, missing = skill_gap_analysis(prediction, text)

    return render_template(
        "resume.html",
        prediction=prediction,
        found_skills=found,
        skill_gap=missing,
        expected_skills=expected
    )

# -----------------------------
# -----------------------------
# QUIZ ROUTES
# -----------------------------
# For now, select the first category automatically
DEFAULT_CATEGORY = list(quiz_questions.keys())[0]

@app.route("/quiz")
def quiz():
    session['score'] = 0
    session['current'] = 0
    session['category'] = DEFAULT_CATEGORY
    return redirect(url_for('question', q_no=0))

@app.route("/question/<int:q_no>", methods=['GET', 'POST'])
def question(q_no):
    category = session['category']
    questions = quiz_questions[category]  # list of questions for this category

    if q_no >= len(questions):
        return redirect(url_for('result'))

    q = questions[q_no]

    if request.method == 'POST':
        selected = request.form.get('option')
        if selected == q['answer']:
            session['score'] += 1
        session['current'] = q_no + 1
        return redirect(url_for('question', q_no=q_no+1))

    return render_template('question.html', question=q, q_no=q_no, total=len(questions))

@app.route("/result")
def result():
    category = session.get('category', DEFAULT_CATEGORY)
    questions = quiz_questions[category]
    score = session.get('score', 0)
    total = len(questions)
    return render_template('result.html', score=score, total=total)

# -----------------------------
# Run app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
