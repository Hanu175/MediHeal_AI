import os
import tempfile

import pandas as pd
import streamlit as st

from services.report_service import ReportService
from services.comparison_service import ComparisonService


def render_comparison_page():

    st.title("📊 Medical Report Comparison")

    st.caption(
        "Compare two laboratory reports. "
        "The comparison shows extracted values only and does not provide diagnosis or treatment advice."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        previous_file = st.file_uploader(
            "Previous Report",
            type=["png", "jpg", "jpeg", "pdf"],
            key="previous_report",
        )

    with col2:

        current_file = st.file_uploader(
            "Current Report",
            type=["png", "jpg", "jpeg", "pdf"],
            key="current_report",
        )

    if previous_file and current_file:

        if st.button(
            "Compare Reports",
            use_container_width=True,
        ):

            with st.spinner("Analyzing reports..."):

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=os.path.splitext(previous_file.name)[1],
                ) as f1:

                    f1.write(previous_file.getbuffer())
                    previous_path = f1.name

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=os.path.splitext(current_file.name)[1],
                ) as f2:

                    f2.write(current_file.getbuffer())
                    current_path = f2.name

                previous = ReportService.parse_medical_report(
                    previous_path
                )

                current = ReportService.parse_medical_report(
                    current_path
                )

                comparison = ComparisonService.compare(
                    previous["json"],
                    current["json"],
                )

            st.success("Comparison Complete")

            df = pd.DataFrame(comparison)

            # -----------------------------
            # Summary Metrics
            # -----------------------------

            increased = 0
            decreased = 0
            unchanged = 0

            for row in comparison:

                if row["direction"] == "▲":
                    increased += 1

                elif row["direction"] == "▼":
                    decreased += 1

                else:
                    unchanged += 1

            total = len(comparison)

            c1, c2, c3, c4 = st.columns(4)

            c1.metric(
                "Tests Compared",
                total,
            )

            c2.metric(
                "▲ Increased",
                increased,
            )

            c3.metric(
                "▼ Decreased",
                decreased,
            )

            c4.metric(
                "→ Unchanged",
                unchanged,
            )

            st.divider()

            # -----------------------------
            # Pretty Table
            # -----------------------------

            display = df.copy()

            display.columns = [

                "Test",

                "Previous",

                "Current",

                "Difference",

                "Direction",

            ]

            st.dataframe(

                display,

                use_container_width=True,

                hide_index=True,

            )

            st.divider()

            # -----------------------------
            # Change Distribution
            # -----------------------------

            chart = pd.DataFrame(

                {

                    "Count": [

                        increased,

                        decreased,

                        unchanged,

                    ]

                },

                index=[

                    "Increased",

                    "Decreased",

                    "Unchanged",

                ],

            )

            st.subheader("📈 Change Distribution")

            st.bar_chart(chart)