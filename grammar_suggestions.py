import requests


def check_grammar(text):
    try:
        response = requests.post(
            "https://api.languagetool.org/v2/check",
            data={
                "text": text,
                "language": "en-US"
            }
        )

        data = response.json()
        mistakes = []

        for match in data.get("matches", []):

            incorrect = text[
                match["offset"]:
                match["offset"] + match["length"]
            ]

            suggestions = []

            if "replacements" in match:
                suggestions = [
                    r["value"]
                    for r in match["replacements"][:3]
                ]

            mistakes.append({
                "message": match["message"],
                "incorrect": incorrect,
                "suggestions": suggestions
            })

        return mistakes

    except Exception as e:
        print("Grammar Error:", e)
        return []