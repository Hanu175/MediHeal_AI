import streamlit as st


def status_card(title, status):

    color = "#22c55e" if status else "#ef4444"

    text = "ONLINE" if status else "OFFLINE"

    st.markdown(
        f"""
        <div style="
            border-left:6px solid {color};
            background:#fafafa;
            padding:14px;
            border-radius:8px;
            margin-bottom:12px;
        ">
            <b>{title}</b><br>
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )