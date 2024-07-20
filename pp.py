import streamlit as st
import json

# إخفاء أزرار GitHub وزر "Manage app" والقائمة الرئيسية
hide_buttons_style = """
    <style>
    .viewerBadge_container__1QSob, footer, #MainMenu, button[title="Manage app"], .css-1cpxqw2 { 
        display: none !important; 
    }
    </style>
"""
st.markdown(hide_buttons_style, unsafe_allow_html=True)

# عنوان للصفحة
st.title('أدخل معلوماتك')

# خانة إدخال النص
user_input = st.text_input("أدخل معلومة هنا:")

# عرض النص الذي أدخله المستخدم
st.write("المعلومة التي أدخلتها هي:", user_input)
