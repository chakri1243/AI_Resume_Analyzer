from skills import skills

def analyze_resume(text):
    text = text.lower()

    score = 0
    found_skills = []

    report = {}

    # Contact Information
    if "@" in text:
        score += 5
        report["Email"] = "Present"
    else:
        report["Email"] = "Missing"

    if any(char.isdigit() for char in text):
        score += 5
        report["Phone"] = "Present"
    else:
        report["Phone"] = "Missing"

    # Education
    education_words = [
        "b.tech",
        "bachelor",
        "degree",
        "cgpa",
        "intermediate",
        "ssc"
    ]

    if any(word in text for word in education_words):
        score += 15
        report["Education"] = "Present"
    else:
        report["Education"] = "Missing"

    # Skills
    skill_score = 0

    for skill in skills:
        if skill.lower() in text:
            found_skills.append(skill)
            skill_score += 2

    if skill_score > 20:
        skill_score = 20

    score += skill_score
    report["Skills"] = f"{len(found_skills)} skills found"

    # Projects
    project_words = [
        "project",
        "developed",
        "implemented",
        "designed"
    ]

    if any(word in text for word in project_words):
        score += 20
        report["Projects"] = "Present"
    else:
        report["Projects"] = "Missing"

    # Certifications
    certification_words = [
        "certificate",
        "certification",
        "coursera",
        "udemy",
        "internship"
    ]

    if any(word in text for word in certification_words):
        score += 10
        report["Certifications"] = "Present"
    else:
        report["Certifications"] = "Missing"

    # Experience
    experience_words = [
        "experience",
        "internship",
        "training"
    ]

    if any(word in text for word in experience_words):
        score += 15
        report["Experience"] = "Present"
    else:
        report["Experience"] = "Missing"

    # Achievements
    achievement_words = [
        "achievement",
        "award",
        "winner",
        "hackathon",
        "activity",
        "leadership"
    ]

    if any(word in text for word in achievement_words):
        score += 10
        report["Achievements"] = "Present"
    else:
        report["Achievements"] = "Missing"

    if score > 100:
        score = 100

    return {
        "score": score,
        "report": report,
        "found": found_skills
    }