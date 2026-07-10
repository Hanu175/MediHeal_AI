import streamlit as st

from services.database_service import DatabaseService
from utils.session_manager import SessionManager
from ui.components.metric_card import metric_card


def render_dashboard():

    st.title("🩺 MediSphere AI")

    st.caption("AI-Powered Multi-Agent Healthcare Assistant")

    st.divider()

    # ----------------------------------
    # Statistics
    # ----------------------------------

    reports = DatabaseService.total_reports()
    medications = DatabaseService.total_medications()
    success = DatabaseService.success_count()
    failed = DatabaseService.failed_count()

    total = success + failed

    success_rate = 100 if total == 0 else round((success / total) * 100)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🩺 Reports", reports)
    c2.metric("💊 Medications", medications)
    c3.metric("🤖 AI Requests", success)
    c4.metric("✅ Success Rate", f"{success_rate}%")
    col1, col2, col3, col4 = st.columns(4)

    # with col1:
    #     metric_card(
    #         "Reports",
    #         reports,
    #         "🩺",
    #     )

    # with col2:
    #     metric_card(
    #         "Medication",
    #         medications,
    #         "💊",
    #     )

    # with col3:
    #     metric_card(
    #         "AI Requests",
    #         success,
    #         "🤖",
    #     )

    # with col4:
    #     metric_card(
    #         "Success",
    #         f"{success_rate}%",
    #         "✅",
    #     )

    st.divider()

    # ----------------------------------
    # Quick Overview
    # ----------------------------------

    left, right = st.columns([1, 1])

    with left:

        st.subheader("⚡ Available Features")

        st.success("🩺 Medical Report Parser")

        st.success("💊 Medication Manager")

        st.success("💬 AI Assistant")

        st.success("📑 Compare Reports")

        st.success("📈 Analytics Dashboard")

        st.success("📜 History")

    with right:

        st.subheader("🕒 Latest Activity")

        activity = DatabaseService.latest_activity()

        if activity:

            st.write(f"**Agent:** {activity.agent}")

            st.write(f"**Status:** {activity.status}")

            if activity.timestamp:
                st.write(f"**Time:** {activity.timestamp}")

            if activity.execution_time:
                st.write(
                    f"**Runtime:** {activity.execution_time:.2f} sec"
                )

        else:

            st.info("No activity yet.")

    st.divider()

    # ----------------------------------
    # Latest Report
    # ----------------------------------

    st.subheader("📄 Latest Report")

    report = SessionManager.get_report()["markdown"]

    if report:

        st.markdown(report[:600])

        if len(report) > 600:

            st.caption("Preview only...")

    else:

        st.info("No report available in this session.")

    st.divider()

    # ----------------------------------
    # Latest Medication
    # ----------------------------------

    st.subheader("💊 Latest Medication")

    medication = SessionManager.get_medication()

    if medication:

        st.markdown(medication[:600])

        if len(medication) > 600:

            st.caption("Preview only...")

    else:

        st.info("No medication schedule available.")

    st.divider()

    # ----------------------------------
    # Active Agents
    # ----------------------------------

    st.subheader("🤖 Active Agents")

    a1, a2, a3 = st.columns(3)

    a1.success("Supervisor")

    a2.success("Report Parser")

    a3.success("Medication Manager")

    st.divider()

    st.caption(
        "MediSphere AI • LangGraph • Gemini • Streamlit • SQLite"
    )