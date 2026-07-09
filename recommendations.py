JAVA_SKILLS = [
    "java",
    "spring boot",
    "hibernate",
    "mysql",
    "rest api",
    "maven",
    "git",
    "docker"
]

PYTHON_SKILLS = [
    "python",
    "flask",
    "django",
    "sql",
    "pandas",
    "numpy",
    "machine learning"
]

DATA_ANALYST_SKILLS = [
    "python",
    "sql",
    "power bi",
    "excel",
    "tableau",
    "statistics"
]


def get_missing_skills(user_skills, role):

    roles = {
        "Java Developer": JAVA_SKILLS,
        "Python Developer": PYTHON_SKILLS,
        "Data Analyst": DATA_ANALYST_SKILLS
    }

    required = roles.get(role, [])

    missing = []

    user_skills = [
        s.lower() for s in user_skills
    ]

    for skill in required:
        if skill not in user_skills:
            missing.append(skill.title())

    return missing