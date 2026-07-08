import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("🩺 MediSphere AI")

        st.caption("AI Powered Healthcare Assistant")

        st.markdown("---")

        st.markdown("### 🤖 Active Agents")

        st.success("Supervisor")

        st.success("Medical Report Parser")

        st.success("Medication Manager")

        st.markdown("---")

        st.markdown("### ⚙ Technology")

        st.markdown("- LangGraph")
        st.markdown("- Gemini")
        st.markdown("- Tesseract OCR")
        st.markdown("- SQLite")

        st.markdown("---")

        st.info(
            """
**Current Version**

Phase 1

**Architecture**

2 Active AI Agents

Built using a modular Service Layer.
"""
        )