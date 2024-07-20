import streamlit as st

# إخفاء الزر البرتقالي باستخدام JavaScript
hide_button_script = """
    <script>
    document.addEventListener("DOMContentLoaded", function() {
        var elements = document.getElementsByClassName('viewerBadge_container_r5tak');
        if (elements.length > 0) {
            elements[0].style.display = 'none';
        }
    });
    </script>
"""
st.markdown(hide_button_script, unsafe_allow_html=True)
