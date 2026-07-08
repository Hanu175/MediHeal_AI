import streamlit as st


PAGES = [

    "🏠 Dashboard",

    "🩺 Medical Report",

    "💊 Medication",

    "📜 History",

    "📊 Analytics",

    "⚙ Settings",

]


def navigation():

    st.sidebar.title("Navigation")

    page = st.sidebar.radio(

        "Navigation",

        PAGES,

        label_visibility="collapsed",

    )

    return page