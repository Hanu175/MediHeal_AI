import streamlit as st

from graph.workflow import graph
from utils.state_factory import create_state
from utils.session_manager import SessionManager


def render_chat_page():

    st.title("💬 AI Assistant")

    st.caption(
        "Ask questions about your uploaded reports, medications, or general healthcare concepts."
    )

    st.divider()

    # -----------------------------
    # Initialize Chat History
    # -----------------------------

    if "chat_history" not in st.session_state:

        st.session_state.chat_history = []

    # -----------------------------
    # Display Chat
    # -----------------------------

    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # -----------------------------
    # User Input
    # -----------------------------

    question = st.chat_input(
        "Ask MediSphere AI..."
    )

    if question is None:

        return

    # -----------------------------
    # User Message
    # -----------------------------

    st.session_state.chat_history.append(

        {

            "role": "user",

            "content": question,

        }

    )

    with st.chat_message("user"):

        st.markdown(question)

    # -----------------------------
    # AI Response
    # -----------------------------

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            state = create_state(

                user_input=question,

                next_agent="chat",

            )

            state["report_summary"] = (
                st.session_state.report_markdown
            )

            state["medication_schedule"] = (
                st.session_state.medication_schedule
            )

            result = graph.invoke(state)

            answer = result["final_response"]

            st.markdown(answer)

    st.session_state.chat_history.append(

        {

            "role": "assistant",

            "content": answer,

        }

    )