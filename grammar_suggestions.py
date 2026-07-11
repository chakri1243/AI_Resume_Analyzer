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

        suggestions = []

        for m in data["matches"]:
            suggestions.append({
                "message": m["message"],
                "suggestion":
                [r["value"] for r in m["replacements"]]
            })

        return suggestions

    except:
        return []