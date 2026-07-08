import streamlit as st


def render_dashboard():

    st.title("🩺 MediSphere AI")

    st.subheader("AI-Powered Healthcare Assistant")

    st.markdown("---")

    st.markdown(
        """
Welcome to **MediSphere AI**.

This application demonstrates a **LangGraph-based Multi-Agent Healthcare Assistant**.

Current Phase: **Phase 1**
"""
    )

    col1, col2 = st.columns(2)

    with col1:

        st.info("🩺 Medical Report Parser")

        st.write(
            "Upload laboratory reports and receive a simple explanation of the extracted laboratory values."
        )

    with col2:

        st.success("💊 Medication Manager")

        st.write(
            "Paste a prescription and generate a structured medication schedule."
        )

    st.markdown("---")

    st.subheader("🤖 Active Agents")

    st.write("✅ Supervisor Agent")

    st.write("✅ Medical Report Parser")

    st.write("✅ Medication Manager")

    st.markdown("---")

    st.subheader("🚀 Upcoming Agents")

    st.write("• Symptom Understanding")

    st.write("• Lifestyle Recommendation")

    st.write("• Healthcare Planner")

    st.write("• Reflection Agent")

    st.write("• Verification Agent")

    st.markdown("---")

    st.success("Project Status: Working Phase 1 Prototype")