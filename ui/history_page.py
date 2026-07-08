import streamlit as st

from services.database_service import DatabaseService


def render_history():

    st.title("📜 Interaction History")

    history = DatabaseService.history()

    if not history:

        st.info("No interactions found.")

        return

    for row in history:

        with st.expander(f"{row.agent}  |  #{row.id}"):

            if hasattr(row, "timestamp") and row.timestamp:

                st.write(f"**Timestamp:** {row.timestamp}")

            if hasattr(row, "status") and row.status:

                st.write(f"**Status:** {row.status}")

            if hasattr(row, "execution_time") and row.execution_time:

                st.write(
                    f"**Execution Time:** {row.execution_time:.2f} seconds"
                )

            st.markdown("---")

            st.subheader("Input")

            st.write(row.user_input)

            st.subheader("Response")

            st.markdown(row.response)