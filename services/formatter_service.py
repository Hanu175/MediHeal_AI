class FormatterService:

    STATUS_ICON = {
        "Within Reference Range": "🟢",
        "Above Reference Range": "🟡",
        "Below Reference Range": "🟠",
        "Cannot Determine": "⚪"
    }

    @staticmethod
    def report_to_markdown(report_json):

        if "tests" not in report_json:
            return "No report data available."

        md = "# 🩺 Medical Report Summary\n\n"

        for test in report_json["tests"]:

            status = test.get("status", "Cannot Determine")
            icon = FormatterService.STATUS_ICON.get(status, "⚪")

            md += f"## {test.get('name', 'Unknown Test')}\n\n"

            md += f"**Value:** {test.get('value', '-')}"
            if test.get("unit"):
                md += f" {test['unit']}"
            md += "\n\n"

            md += f"**Reference Range:** {test.get('reference_range', '-')}\n\n"

            md += f"**Status:** {icon} {status}\n\n"

            md += f"**Explanation:**\n\n"

            md += f"{test.get('explanation', '-')}\n\n"

            md += "---\n\n"

        md += (
            "_This explanation is informational only and is "
            "not a diagnosis or medical advice._"
        )

        return md