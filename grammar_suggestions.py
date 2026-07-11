import language_tool_python

tool = language_tool_python.LanguageTool(
    'en-US'
)


def check_grammar(text):

    matches = tool.check(text)

    mistakes = []

    for m in matches:

        mistakes.append(
            {
                "message": m.message,
                "incorrect": m.context
            }
        )

    return mistakes