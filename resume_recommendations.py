def generate_recommendations(result):

    recommendations = []

    # LinkedIn
    if not result.get('linkedin'):
        recommendations.append(
            "Add your LinkedIn profile URL to make your resume more professional."
        )

    # GitHub
    if not result.get('github'):
        recommendations.append(
            "Add your GitHub profile URL to showcase your projects and coding skills."
        )

    # Education
    if not result.get('education'):
        recommendations.append(
            "Add your education details including degree, college, and graduation year."
        )

    # CGPA
    if not result.get('cgpa'):
        recommendations.append(
            "Mention your CGPA or percentage in the education section."
        )

    # Skills
    skills = result.get('skills', [])

    if isinstance(skills, list):
        if len(skills) < 5:
            recommendations.append(
                "Add more technical skills related to your domain."
            )
    elif not skills:
        recommendations.append(
            "Add technical skills to improve your ATS score."
        )

    # Projects
    projects = result.get('projects')

    if not projects:
        recommendations.append(
            "Add at least two projects with technologies used and project descriptions."
        )

    # Certifications
    certifications = result.get('certifications')

    if not certifications:
        recommendations.append(
            "Add certifications to improve your ATS score."
        )

    # Activities / Achievements
    activities = result.get('activities')

    if not activities:
        recommendations.append(
            "Add achievements, extracurricular activities, or positions of responsibility."
        )

    # Experience
    experience = result.get('experience')

    if not experience:
        recommendations.append(
            "Add internships, practical experience, or training programs."
        )

    # General recommendations
    recommendations.append(
        "Use action words like Developed, Designed, Implemented, Built, and Optimized."
    )

    recommendations.append(
        "Quantify your achievements with numbers and percentages whenever possible."
    )

    recommendations.append(
        "Keep your resume length between 1 and 2 pages."
    )

    recommendations.append(
        "Use clear section headings and a professional format."
    )

    return recommendations


def predicted_score(result):

    score = result.get('ats_score', 0)

    if not result.get('linkedin'):
        score += 2

    if not result.get('github'):
        score += 2

    if not result.get('certifications'):
        score += 5

    if not result.get('projects'):
        score += 5

    if not result.get('experience'):
        score += 5

    if not result.get('activities'):
        score += 3

    if score > 100:
        score = 100

    return score