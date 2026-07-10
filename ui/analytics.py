import streamlit as st
import pandas as pd

from services.database_service import DatabaseService


def render_analytics():

    st.title("📊 MediSphere AI Analytics")
    st.caption("Live insights from your MediSphere AI platform")

    history = DatabaseService.history()

    reports = DatabaseService.total_reports()
    medications = DatabaseService.total_medications()
    success = DatabaseService.success_count()
    failed = DatabaseService.failed_count()
    avg_runtime = DatabaseService.average_runtime()

    total_requests = success + failed

    success_rate = (
        round((success / total_requests) * 100, 1)
        if total_requests > 0
        else 0
    )

    # ==========================================
    # KPI CARDS
    # ==========================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🩺 Reports Parsed",
            reports
        )

    with col2:
        st.metric(
            "💊 Medication Plans",
            medications
        )

    with col3:
        st.metric(
            "✅ Success Rate",
            f"{success_rate}%"
        )

    with col4:
        st.metric(
            "⚡ Avg Runtime",
            f"{avg_runtime:.2f}s"
        )

    st.divider()

    # ==========================================
    # LATEST ACTIVITY
    # ==========================================

    latest = DatabaseService.latest_activity()

    col1, col2 = st.columns([2, 1])

    with col1:

        st.subheader("🕒 Latest Activity")

        if latest:

            st.info(
                f"""
**Agent**

{latest.agent}

---

**Status**

{latest.status}

---

**Runtime**

{latest.execution_time if latest.execution_time else "N/A"} sec

---

**Timestamp**

{latest.timestamp}
"""
            )

        else:

            st.warning("No activity recorded yet.")

    # ==========================================
    # AGENT USAGE
    # ==========================================

    with col2:

        st.subheader("📈 Agent Usage")

        if history:

            counts = {}

            for row in history:

                counts[row.agent] = counts.get(
                    row.agent,
                    0,
                ) + 1

            df = pd.DataFrame(

                {

                    "Agent": list(counts.keys()),

                    "Requests": list(counts.values())

                }

            )

            st.bar_chart(
                df.set_index("Agent")
            )

        else:

            st.info("No data")

    st.divider()

    # ==========================================
    # RUNTIME TREND
    # ==========================================

    st.subheader("⚡ Runtime Trend")

    runtime = []

    for row in reversed(history):

        if row.execution_time:

            runtime.append(row.execution_time)

    if runtime:

        runtime_df = pd.DataFrame(

            {

                "Execution Time (sec)": runtime

            }

        )

        st.line_chart(runtime_df)

    else:

        st.info("No runtime data available.")

    st.divider()

    # ==========================================
    # RECENT REQUESTS
    # ==========================================

    st.subheader("📜 Recent Requests")

    if history:

        table = []

        for row in history[:10]:

            table.append(

                {

                    "Agent": row.agent,

                    "Status": row.status,

                    "Runtime (sec)": row.execution_time,

                    "Timestamp": row.timestamp,

                }

            )

        df = pd.DataFrame(table)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
        )

    else:

        st.info("No requests available.")