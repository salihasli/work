import streamlit as st
import json

# إخفاء الزر البرتقالي
hide_orange_button_style = """
    <style>
    .viewerBadge_link_qRIco {
        display: none !important;
    }
    </style>
"""
st.markdown(hide_orange_button_style, unsafe_allow_html=True)


# عنوان للصفحة
st.title('أدخل معلوماتك')

# خانة إدخال النص
user_input = st.text_input("أدخل معلومة هنا:")

# عرض النص الذي أدخله المستخدم
st.write("المعلومة التي أدخلتها هي:", user_input)
