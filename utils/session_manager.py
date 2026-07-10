import streamlit as st


class SessionManager:

    # ---------------------------------
    # Initialize Session
    # ---------------------------------

    @staticmethod
    def initialize():

        defaults = {

            # Latest Report
            "report_json": None,
            "report_markdown": None,

            # Latest Medication
            "medication_schedule": None,

            # Latest Comparison
            "comparison_result": None,

            # Chat History
            "chat_history": [],

            # Last Active Agent
            "last_agent": None,
            "current_page": "🏠 Dashboard",

        }

        for key, value in defaults.items():

            if key not in st.session_state:

                st.session_state[key] = value

    # ---------------------------------
    # Report
    # ---------------------------------

    @staticmethod
    def save_report(report_json, report_markdown):

        st.session_state.report_json = report_json
        st.session_state.report_markdown = report_markdown
        st.session_state.last_agent = "Report Parser"

    @staticmethod
    def get_report():

        return {
            "json": st.session_state.report_json,
            "markdown": st.session_state.report_markdown,
        }

    # ---------------------------------
    # Medication
    # ---------------------------------

    @staticmethod
    def save_medication(schedule):

        st.session_state.medication_schedule = schedule
        st.session_state.last_agent = "Medication Manager"

    @staticmethod
    def get_medication():

        return st.session_state.medication_schedule

    # ---------------------------------
    # Comparison
    # ---------------------------------

    @staticmethod
    def save_comparison(comparison):

        st.session_state.comparison_result = comparison
        st.session_state.last_agent = "Comparison"

    @staticmethod
    def get_comparison():

        return st.session_state.comparison_result

    # ---------------------------------
    # Chat
    # ---------------------------------

    @staticmethod
    def add_chat(role, content):

        st.session_state.chat_history.append(

            {

                "role": role,

                "content": content,

            }

        )

    @staticmethod
    def get_chat():

        return st.session_state.chat_history

    @staticmethod
    def clear_chat():

        st.session_state.chat_history = []

    # ---------------------------------
    # Last Active Agent
    # ---------------------------------

    @staticmethod
    def get_last_agent():

        return st.session_state.last_agent

    # ---------------------------------
    # Clear Everything
    # ---------------------------------

    @staticmethod
    def clear():

        st.session_state.report_json = None
        st.session_state.report_markdown = None
        st.session_state.medication_schedule = None
        st.session_state.comparison_result = None
        st.session_state.chat_history = []
        st.session_state.last_agent = None
        
    # ---------------------------------
    # Navigation
    # ---------------------------------

    @staticmethod
    def navigate(page):

        st.session_state.current_page = page


    @staticmethod
    def get_page():

        return st.session_state.get(
            "current_page",
            "🏠 Dashboard"
        )