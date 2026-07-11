def recommend_projects(skills):

    projects = []

    if "python" in str(skills).lower():

        projects.append(
            "AI Resume Analyzer"
        )

        projects.append(
            "Chatbot using Generative AI"
        )

    if "machine learning" in str(skills).lower():

        projects.append(
            "Fake News Detection"
        )

        projects.append(
            "Movie Recommendation System"
        )

    if "data analysis" in str(skills).lower():

        projects.append(
            "Sales Dashboard using Power BI"
        )

    return projects