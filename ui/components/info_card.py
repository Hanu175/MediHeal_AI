import streamlit as st


def info_card(title, body):

    st.markdown(
        f"""
        <div style="
            border:1px solid #dddddd;
            border-radius:10px;
            padding:16px;
            margin-bottom:14px;
        ">
            <h4>{title}</h4>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )