import streamlit as st

# إخفاء الزر البرتقالي باستخدام CSS وJavaScript
hide_button_script = """
    <style>
    .viewerBadge_container__r5tak,
    .styles_viewerBadge__CvC9N,
    .viewerBadge_link__qRIco,
    .viewerBadge_container {
        display: none !important;
    }
    </style>
    <script>
    document.addEventListener("DOMContentLoaded", function() {
        var elements = document.querySelectorAll('.viewerBadge_container__r5tak, .styles_viewerBadge__CvC9N, .viewerBadge_link__qRIco, .viewerBadge_container');
        elements.forEach(function(element) {
            element.style.display = 'none';
        });
    });
    </script>
"""
st.markdown(hide_button_script, unsafe_allow_html=True)

# إضافة خانة إدخال
st.title('أدخل معلوماتك')
user_input = st.text_input("أدخل معلومة هنا:")
st.write(" التي أدخلتها هي:", user_input)
