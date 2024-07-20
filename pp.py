import streamlit as st

# إخفاء الزر البرتقالي الذي يظهر في الزاوية السفلية اليمنى
hide_orange_button_style = """
    <style>
    .viewerBadge_container_r5tak {
        display: none !important;
    }
    </style>
"""
st.markdown(hide_orange_button_style, unsafe_allow_html=True)
