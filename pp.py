import streamlit as st

# إضافة طبقة لتغطية الزر البرتقالي
cover_badge_script = """
    <style>
    .cover-badge {
        position: fixed;
        bottom: 0;
        right: 0;
        width: 50px;
        height: 50px;
        background-color: white;
        z-index: 9999;
    }
    </style>
    <div class='cover-badge'></div>
"""
st.markdown(cover_badge_script, unsafe_allow_html=True)

# إضافة خانة إدخال
st.title('أدخل معلوماتك')
user_input = st.text_input("أدخل معلومة هنا:")
st.write("المعلومة التي أدخلتها هي:", user_input)
