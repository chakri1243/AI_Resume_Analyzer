from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)


def calculate_match(
        resume,
        jd):

    documents = [
        resume,
        jd
    ]

    tfidf = TfidfVectorizer()

    matrix = tfidf.fit_transform(
        documents
    )

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )

    return round(
        similarity[0][0] * 100,
        2
    )