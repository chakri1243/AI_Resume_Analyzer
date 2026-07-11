def improve_resume(result):

    suggestions = []

    score = result.get(
        'ats_score',
        0
    )

    skills = result.get(
        'skills',
        []
    )

    projects = result.get('projects', [])

    if isinstance(projects, bool):
        projects = []

    certifications = result.get('certifications', [])
    if isinstance(certifications, bool):
        certifications = []

    experience = result.get('experience', [])
    if isinstance(experience, bool):
        experience = []

    activities = result.get('activities', [])
    if isinstance(activities, bool):
        activities = []

    # Skills

    if len(skills) < 8:

        suggestions.append(
            "Add at least 8-10 technical skills to improve ATS score."
        )

    # Projects

    if not projects:

        suggestions.append(
            "Add at least 2 real-world projects."
        )

    elif len(projects) < 2:

        suggestions.append(
            "Your projects are too few. Add more projects."
        )

    # Certifications

    if not certifications:

        suggestions.append(
            "Add certifications from Coursera, Google, IBM or Microsoft."
        )

    # Experience

    if not experience:

        suggestions.append(
            "Add internships or practical experience."
        )

    # Achievements

    if not activities:

        suggestions.append(
            "Add achievements and extracurricular activities."
        )

    # ATS improvement levels

    if score < 60:

        suggestions.append(
            "Your resume needs major improvements to cross 85% ATS score."
        )

    elif score < 75:

        suggestions.append(
            "Your resume is good but needs improvements to reach 85% ATS score."
        )

    elif score < 85:

        suggestions.append(
            "Your resume is very close to 85%. Add some advanced skills and projects."
        )

    # Future skills

    future_skills = [
        "Generative AI",
        "Prompt Engineering",
        "Machine Learning",
        "Docker",
        "AWS",
        "Git",
        "LangChain",
        "Power BI",
        "System Design"
    ]

    missing = []

    for skill in future_skills:

        if skill.lower() not in [
            s.lower()
            for s in skills
        ]:

            missing.append(skill)

    return suggestions, missing