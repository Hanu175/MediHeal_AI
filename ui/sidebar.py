import streamlit as st

from utils.session_manager import SessionManager


def render_sidebar():

    with st.sidebar:

        st.title("🩺 MediSphere AI")

        st.caption("AI Healthcare Assistant")

        st.divider()

        # -----------------------------
        # System Status
        # -----------------------------

        st.subheader("📡 System Status")

        st.success("🟢 Database Connected")

        st.success("🟢 Session Active")

        if SessionManager.get_report()["markdown"]:

            st.success("🟢 Report Loaded")

        else:

            st.warning("🟡 No Report")

        if SessionManager.get_medication():

            st.success("🟢 Medication Loaded")

        else:

            st.warning("🟡 No Medication")

        st.divider()

        # -----------------------------
        # Last Agent
        # -----------------------------

        st.subheader("🤖 Last Active Agent")

        agent = SessionManager.get_last_agent()

        if agent:

            st.info(agent)

        else:

            st.caption("No activity yet.")

        st.divider()

        st.subheader("⚙ Technology")

        st.write("• LangGraph")

        st.write("• Gemini")

        st.write("• Streamlit")

        st.write("• SQLite")

        st.write("• OCR")

        st.divider()

        st.caption("Version 2.0.0")