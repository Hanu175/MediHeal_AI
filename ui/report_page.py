import os
import streamlit as st

from graph.workflow import graph
from utils.state_factory import create_state

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


def render_report_page():

    st.title("🩺 Medical Report Parser")

    st.write(
        "Upload a laboratory report image. MediSphere AI will extract the laboratory values and provide a simple explanation."
    )

    st.info(
        "Supported formats: PNG, JPG, JPEG"
    )

    uploaded_file = st.file_uploader(
        "Upload Medical Report",
        type=["png", "jpg", "jpeg"],
        key="report_upload",
    )

    if uploaded_file is None:

        st.warning("Please upload a medical report to begin analysis.")

        return

    save_path = os.path.join(
        UPLOAD_DIR,
        uploaded_file.name,
    )

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(
        uploaded_file,
        caption="Uploaded Report",
        use_container_width=True,
    )

    st.divider()

    if st.button(
        "🔍 Analyze Report",
        use_container_width=True,
    ):

        with st.spinner("Analyzing report..."):

            state = create_state(
                user_input="Explain this medical report",
                uploaded_report_path=save_path,
                next_agent="report",
            )

            result = graph.invoke(state)

        st.success("Analysis Completed")

        st.markdown(result["final_response"])

        st.download_button(
            label="📥 Download Report",
            data=result["final_response"],
            file_name="medical_report.md",
            mime="text/markdown",
            use_container_width=True,
        )