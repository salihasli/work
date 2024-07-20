import streamlit as st

# إخفاء الزر البرتقالي باستخدام CSS وJavaScript
hide_button_style = """
    <style>
    .viewerBadge_container__r5tak,
    .styles_viewerBadge__CvC9N,
    .viewerBadge_link__qRIco {
        display: none !important;
    }
    </style>
    <script>
    document.addEventListener("DOMContentLoaded", function() {
        var elements = document.getElementsByClassName('viewerBadge_container__r5tak');
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.display = 'none';
        }
        var elements2 = document.getElementsByClassName('styles_viewerBadge__CvC9N');
        for (var i = 0; i < elements2.length; i++) {
            elements2[i].style.display = 'none';
        }
        var elements3 = document.getElementsByClassName('viewerBadge_link__qRIco');
        for (var i = 0; i < elements3.length; i++) {
            elements3[i].style.display = 'none';
        }
    });
    </script>
"""
st.markdown(hide_button_style, unsafe_allow_html=True)

# إضافة خانة إدخال
st.title('أدخل معلوماتك')
user_input = st.text_input("أدخل معلومة هنا:")
st.write("المعلومة التي أدخلتها هي:", user_input)
