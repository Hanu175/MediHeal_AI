from datetime import datetime
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)


class PDFService:

    @staticmethod
    def generate_report(
        report_markdown: str,
        output_path: str,
    ):

        styles = getSampleStyleSheet()

        document = SimpleDocTemplate(
            output_path
        )

        elements = []

        title = Paragraph(
            "<b><font size=18>🩺 MediSphere AI</font></b>",
            styles["Title"],
        )

        elements.append(title)

        elements.append(Spacer(1, 20))

        subtitle = Paragraph(
            "<b>Medical Report Summary</b>",
            styles["Heading2"],
        )

        elements.append(subtitle)

        elements.append(Spacer(1, 10))

        generated = Paragraph(

            f"""
Generated On:
{datetime.now().strftime("%d %B %Y %I:%M %p")}
""",

            styles["Normal"],
        )

        elements.append(generated)

        elements.append(Spacer(1, 20))

        lines = report_markdown.split("\n")

        for line in lines:

            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):

                text = line.replace("#", "").strip()

                elements.append(
                    Paragraph(
                        f"<b>{text}</b>",
                        styles["Heading2"],
                    )
                )

            elif line.startswith("-"):

                text = line.replace("-", "").strip()

                elements.append(
                    Paragraph(
                        "• " + text,
                        styles["Normal"],
                    )
                )

            else:

                elements.append(
                    Paragraph(
                        line,
                        styles["Normal"],
                    )
                )

        elements.append(Spacer(1, 25))

        disclaimer = Paragraph(
            """
<b>Disclaimer</b><br/><br/>

This report was generated automatically by
MediSphere AI.

It is intended only for educational and
informational purposes.

It does not provide medical diagnosis,
treatment recommendations, or emergency
guidance.
""",
            styles["Italic"],
        )

        elements.append(disclaimer)

        document.build(elements)

        return output_path