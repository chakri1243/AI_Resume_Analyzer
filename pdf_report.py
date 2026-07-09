from reportlab.pdfgen import canvas


def create_report(
        score,
        filename):

    c = canvas.Canvas(filename)

    c.drawString(
        100,
        750,
        f"ATS Score : {score}"
    )

    c.save()