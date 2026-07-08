import streamlit as st

from graph.workflow import graph
from utils.state_factory import create_state


def render_medication_page():

    st.title("💊 Medication Management")

    st.write(
        "Paste your prescription below. MediSphere AI will organize the medicines into a simple schedule."
    )

    prescription = st.text_area(
        "Prescription",
        height=220,
        key="medicine_box",
    )

    if prescription.strip() == "":

        st.info("Enter a prescription to begin.")

        return

    if st.button(
        "Generate Medication Schedule",
        use_container_width=True,
    ):

        with st.spinner("Generating schedule..."):

            state = create_state(
                user_input=prescription,
                medication_input=prescription,
                next_agent="medication",
            )

            result = graph.invoke(state)

        st.success("Medication Schedule Generated")

        st.markdown(result["final_response"])

        st.download_button(
            label="📥 Download Schedule",
            data=result["final_response"],
            file_name="medication_schedule.md",
            mime="text/markdown",
            use_container_width=True,
        )