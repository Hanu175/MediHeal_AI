import os

import streamlit as st

from graph.workflow import graph
from utils.state_factory import create_state
from utils.session_manager import SessionManager

from services.pdf_service import PDFService


UPLOAD_DIR = "uploads"
PDF_DIR = "generated_reports"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)


def render_report_page():

    st.header("🩺 Medical Report Parser")

    uploaded_file = st.file_uploader(

        "Upload Blood Report",

        type=["png", "jpg", "jpeg"],

        key="report_upload",

    )

    if uploaded_file is None:

        return

    save_path = os.path.join(

        UPLOAD_DIR,

        uploaded_file.name,

    )

    with open(save_path, "wb") as f:

        f.write(uploaded_file.getbuffer())

    st.image(

        uploaded_file,

        use_container_width=True,

    )

    if st.button(

        "🔍 Analyze Report",

        use_container_width=True,

    ):

        with st.spinner("Analyzing report..."):

            state = create_state(

                user_input="Analyze medical report",

                uploaded_report_path=save_path,

                next_agent="report",

            )

            result = graph.invoke(state)
            st.write(result)
            # -----------------------------------
            # Save to Session Memory
            # -----------------------------------

            SessionManager.save_report(

                result.get("report_json"),

                result.get("report_summary"),

            )

        st.success("Analysis Complete")

        st.markdown(result["final_response"])

        # -----------------------------------
        # Markdown Download
        # -----------------------------------

        st.download_button(

            "⬇ Download Markdown",

            result["final_response"],

            file_name="report.md",

            mime="text/markdown",

            use_container_width=True,

        )

        # -----------------------------------
        # PDF Generation
        # -----------------------------------

        pdf_path = os.path.join(

            PDF_DIR,

            uploaded_file.name.replace(".", "_") + ".pdf",

        )

        PDFService.generate_report(

            result["final_response"],

            pdf_path,

        )

        with open(pdf_path, "rb") as pdf:

            st.download_button(

                "📄 Download Professional PDF",

                data=pdf,

                file_name="MediSphere_Report.pdf",

                mime="application/pdf",

                use_container_width=True,

            )

        # -----------------------------------
        # DEBUG (Temporary)
        # -----------------------------------

        st.divider()

        st.subheader("🧪 Session Debug")

        st.write("Report JSON")

        st.json(st.session_state.report_json)

        st.write("Report Markdown")

        st.markdown(st.session_state.report_markdown)