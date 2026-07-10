import streamlit as st


PAGES = {
    "🏠 Dashboard": "dashboard",
    "🩺 Medical Report": "report",
    "💬 AI Assistant": "chat",
    "📊 Compare Reports": "compare",
    "💊 Medication": "medication",
    "📜 History": "history",
    "📈 Analytics": "analytics",
    "⚙ Settings": "settings",
}


def navigation():

    st.sidebar.title("Navigation")

    page = st.sidebar.radio(

        "Navigation",

        PAGES,

        label_visibility="collapsed",

    )

    return page