import streamlit as st

# إخفاء الزر البرتقالي الذي يظهر في الزاوية السفلية اليمنى
hide_orange_button_style = """
    <style>
    .viewerBadge_container__r5tak,
    .styles_viewerBadge__CvC9N,
    .viewerBadge_link__qRIco {
        display: none !important;
    }
    </style>
"""
st.markdown(hide_orange_button_style, unsafe_allow_html=True)
