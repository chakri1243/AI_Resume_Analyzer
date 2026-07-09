import re


def generate_recommendations(result, text):

    recommendations = []

    # LinkedIn
    if not re.search(
        r'linkedin\.com',
        text.lower()
    ):
        recommendations.append(
            "Add your LinkedIn profile URL."
        )

    # GitHub
    if not re.search(
        r'github\.com',
        text.lower()
    ):
        recommendations.append(
            "Add your GitHub profile URL."
        )

    # Skills
    skills = result.get(
        'skills',
        []
    )

    if len(skills) < 5:

        recommendations.append(
            f"Your resume contains only {len(skills)} skills. Add more relevant technical skills."
        )

    # Projects
    if not result.get(
        'projects'
    ):

        recommendations.append(
            "Add at least two projects with technologies used and descriptions."
        )

    # Certifications
    if not result.get(
        'certifications'
    ):

        recommendations.append(
            "Add certifications to improve your ATS score."
        )

    # Achievements
    if not result.get(
        'activities'
    ):

        recommendations.append(
            "Add achievements or extracurricular activities."
        )

    # Experience
    if not result.get(
        'experience'
    ):

        recommendations.append(
            "Add internships or practical experience."
        )

    # Contact Number
    phone = re.search(
        r'\d{10}',
        text
    )

    if not phone:

        recommendations.append(
            "Add a contact number."
        )

    # Email
    email = re.search(
        r'[\w\.-]+@[\w\.-]+',
        text
    )

    if not email:

        recommendations.append(
            "Add an email address."
        )

    # Resume Length
    words = len(
        text.split()
    )

    if words < 250:

        recommendations.append(
            "Resume is too short. Add more details about projects and skills."
        )

    elif words > 900:

        recommendations.append(
            "Resume is too long. Keep it between 1-2 pages."
        )

    # Action Words
    action_words = [
        "developed",
        "designed",
        "implemented",
        "built",
        "created",
        "optimized"
    ]

    found = False

    for word in action_words:

        if word in text.lower():
            found = True
            break

    if not found:

        recommendations.append(
            "Use action words like Developed, Designed, Implemented, Built, and Optimized."
        )

    return recommendations