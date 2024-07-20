import streamlit as st

# إخفاء الزر البرتقالي باستخدام JavaScript فقط
hide_button_script = """
    <script>
    document.addEventListener("DOMContentLoaded", function() {
        var element = document.querySelector('.viewerBadge_container__r5tak');
        if (element) {
            element.style.display = 'none';
        }
    });
    </script>
"""
st.markdown(hide_button_script, unsafe_allow_html=True)

# إضافة خانة إدخال
st.title('أدخل معلوماتك')
user_input = st.text_input("أدخل معلومة هنا:")
st.write(" التي أدخلتها هي:", user_input)
