import streamlit as st

# إخفاء الزر البرتقالي
hide_orange_button_style = """
    <style>
    .viewerBadge_link_qRIco {
        display: none !important;
    }
    </style>
"""
st.markdown(hide_orange_button_style, unsafe_allow_html=True)
