import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch


def generate_pdf(prediction):

    os.makedirs("reports", exist_ok=True)

    pdf_path = os.path.join(
        "reports",
        f"report_{prediction.prediction_id}.pdf"
    )

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    title = styles["Heading1"]
    title.alignment = TA_CENTER

    story = []

    # -----------------------------
    # Title
    # -----------------------------

    story.append(
        Paragraph(
            "VisionCare AI",
            title
        )
    )

    story.append(
        Paragraph(
            "AI Medical Image Analysis Report",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1, 20))

    # -----------------------------
    # Patient Details Table
    # -----------------------------

    table_data = [

        ["Patient", prediction.user.name],

        ["Disease", prediction.disease_name],

        ["Confidence", f"{prediction.confidence_score:.2f}%"],

        ["Prediction Date", str(prediction.prediction_date)]

    ]

    table = Table(
        table_data,
        colWidths=[140, 300]
    )

    table.setStyle(TableStyle([

        ("BACKGROUND", (0,0), (-1,0), colors.lightblue),

        ("GRID", (0,0), (-1,-1), 1, colors.grey),

        ("BACKGROUND", (0,0), (0,-1), colors.whitesmoke),

        ("FONTNAME", (0,0), (-1,-1), "Helvetica"),

        ("BOTTOMPADDING", (0,0), (-1,-1), 8)

    ]))

    story.append(table)

    story.append(Spacer(1,20))

    # -----------------------------
    # Uploaded Image
    # -----------------------------

    image_path = os.path.join(
        "static",
        "uploads",
        prediction.image_path
    )

    if os.path.exists(image_path):

        img = Image(
            image_path,
            width=3.5*inch,
            height=3.5*inch
        )

        story.append(
            Paragraph(
                "<b>Uploaded Chest X-ray</b>",
                styles["Heading3"]
            )
        )

        story.append(img)

        story.append(Spacer(1,20))

    # -----------------------------
    # AI Explanation
    # -----------------------------

    story.append(
        Paragraph(
            "<b>AI Medical Explanation</b>",
            styles["Heading3"]
        )
    )

    story.append(
        Paragraph(
            prediction.ai_summary,
            styles["BodyText"]
        )
    )

    story.append(Spacer(1,20))

    # -----------------------------
    # Disclaimer
    # -----------------------------

    story.append(
        Paragraph(
            "<b>Disclaimer</b>",
            styles["Heading3"]
        )
    )

    story.append(
        Paragraph(
            "This report was generated using VisionCare AI. "
            "It is intended for educational purposes only and "
            "should not replace professional medical advice.",
            styles["BodyText"]
        )
    )

    doc.build(story)

    return pdf_path