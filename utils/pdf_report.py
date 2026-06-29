from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_report(
    healthy,
    moderate,
    stressed,
    prediction
):

    pdf = SimpleDocTemplate(
        "outputs/agri_report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Agricultural Intelligence Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"Healthy Vegetation: {healthy}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Moderate Vegetation: {moderate}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Stressed Vegetation: {stressed}%",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"Yield Forecast: {prediction}",
            styles["Heading2"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    try:

        content.append(
            Image(
                "outputs/ndvi_map.png",
                width=300,
                height=300
            )
        )

    except:

        pass

    pdf.build(
        content
    )

    return (
        "outputs/agri_report.pdf"
    )