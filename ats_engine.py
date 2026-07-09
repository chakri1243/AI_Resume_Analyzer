from grammar import grammar_score


def calculate_ats(result, text):

    score = 0
    breakdown = {}
    suggestions = []

    contact = 0

    if result["email"] != "Not Found":
        contact += 5

    if result["phone"] != "Not Found":
        contact += 5

    breakdown["Contact"] = contact
    score += contact

    skills = min(
        len(result["skills"]) * 2,
        20
    )

    breakdown["Skills"] = skills
    score += skills

    education = 10 if result[
        "education"
    ] else 0

    breakdown["Education"] = education
    score += education

    projects = 15 if result[
        "projects"
    ] else 0

    breakdown["Projects"] = projects
    score += projects

    experience = 10 if result[
        "experience"
    ] else 0

    breakdown["Experience"] = experience
    score += experience

    certifications = 10 if result[
        "certifications"
    ] else 0

    breakdown[
        "Certifications"
    ] = certifications

    score += certifications

    achievements = 5 if result[
        "achievements"
    ] else 0

    breakdown[
        "Achievements"
    ] = achievements

    score += achievements

    links = 0

    if result[
        "linkedin"
    ] != "Not Found":
        links += 2

    if result[
        "github"
    ] != "Not Found":
        links += 3

    breakdown["Links"] = links
    score += links

    grammar = grammar_score(text)

    breakdown["Grammar"] = grammar
    score += grammar

    if not result["projects"]:
        suggestions.append(
            "Add at least two projects."
        )

    if not result[
            "certifications"]:
        suggestions.append(
            "Add certifications."
        )

    if result[
            "github"] == "Not Found":
        suggestions.append(
            "Add GitHub profile."
        )

    if result[
            "linkedin"] == "Not Found":
        suggestions.append(
            "Add LinkedIn profile."
        )

    return {
        "ats_score": score,
        "breakdown": breakdown,
        "suggestions": suggestions
    }