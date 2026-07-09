def grammar_score(text):

    words = len(text.split())

    if words > 500:
        return 5
    elif words > 400:
        return 4
    elif words > 300:
        return 3
    elif words > 200:
        return 2
    else:
        return 1