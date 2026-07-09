import re
from skills import skills


def analyze_resume(text):

    text_lower = text.lower()

    result = {}

    email = re.findall(
        r'[\w\.-]+@[\w\.-]+',
        text
    )

    result["email"] = (
        email[0]
        if email else
        "Not Found"
    )

    phone = re.findall(
        r'\d{10}',
        text
    )

    result["phone"] = (
        phone[0]
        if phone else
        "Not Found"
    )

    linkedin = re.findall(
        r'linkedin\.com\S+',
        text_lower
    )

    result["linkedin"] = (
        linkedin[0]
        if linkedin else
        "Not Found"
    )

    github = re.findall(
        r'github\.com\S+',
        text_lower
    )

    result["github"] = (
        github[0]
        if github else
        "Not Found"
    )

    found_skills = []

    for skill in skills:

        if skill.lower() in text_lower:
            found_skills.append(skill)

    result["skills"] = found_skills

    result["education"] = (
        "b.tech" in text_lower
        or
        "degree" in text_lower
        or
        "cgpa" in text_lower
    )

    result["projects"] = (
        "project" in text_lower
    )

    result["experience"] = (
        "internship" in text_lower
        or
        "experience" in text_lower
    )

    result["certifications"] = (
        "certificate" in text_lower
        or
        "certification" in text_lower
    )

    result["achievements"] = (
        "achievement" in text_lower
        or
        "award" in text_lower
        or
        "winner" in text_lower
    )

    return result