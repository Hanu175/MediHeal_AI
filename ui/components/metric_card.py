import streamlit as st


def metric_card(title, value, icon="📊"):

    st.markdown(
        f"""
        <div style="
            border:1px solid rgba(128,128,128,0.25);
            border-radius:12px;
            padding:18px;
            background:var(--secondary-background-color);
            color:var(--text-color);
            box-shadow:0 2px 8px rgba(0,0,0,0.10);
            text-align:center;
            margin-bottom:12px;
        ">

            <div style="
                font-size:18px;
                font-weight:600;
                margin-bottom:10px;
            ">
                {icon} {title}
            </div>

            <div style="
                font-size:38px;
                font-weight:700;
            ">
                {value}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )