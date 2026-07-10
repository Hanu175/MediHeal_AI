import streamlit as st

# -----------------------------
# Initialize Database
# -----------------------------
from database.db import init_db

init_db()

from utils.session_manager import SessionManager

SessionManager.initialize()
# -----------------------------
# UI Imports
# -----------------------------
from ui.sidebar import render_sidebar
from ui.navigation import navigation

from ui.dashboard import render_dashboard
from ui.report_page import render_report_page
from ui.medication_page import render_medication_page
from ui.history_page import render_history

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="MediSphere AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown(
    """
<style>

.main{
    padding-top:20px;
}

.stButton>button{
    width:100%;
    height:45px;
    border-radius:10px;
    font-size:16px;
    font-weight:bold;
}

.stDownloadButton>button{
    width:100%;
    border-radius:10px;
}

.footer{
    text-align:center;
    color:gray;
    font-size:14px;
}

</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Sidebar
# -----------------------------
render_sidebar()

# -----------------------------
# Navigation
# -----------------------------
page = navigation()

# -----------------------------
# Routing
# -----------------------------
if page == "🏠 Dashboard":

    render_dashboard()

elif page == "🩺 Medical Report":

    render_report_page()

elif page == "💊 Medication":

    render_medication_page()
    
elif page == "💬 AI Assistant":

    from ui.chat_page import render_chat_page

    render_chat_page()

elif page == "📜 History":

    render_history()

elif page == "📈 Analytics":

    from ui.analytics import render_analytics

    render_analytics()

elif page == "⚙ Settings":

    st.title("⚙ Settings")

    st.info("Settings page is under development.")
    
elif page == "📊 Compare Reports":

    from ui.comparison_page import render_comparison_page

    render_comparison_page()

else:

    st.error("Unknown page selected.")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.markdown(
    """
<div class="footer">

Developed using

<b>Streamlit</b> •
<b>LangGraph</b> •
<b>Gemini</b> •
<b>Tesseract OCR</b> •
<b>SQLite</b>

</div>
""",
    unsafe_allow_html=True,
)