import streamlit as st

# Hide the Streamlit hosted button using CSS and JavaScript
hide_button_script = """
    <style>
    .viewerBadge_container__r5tak,
    .styles_viewerBadge__CvC9N,
    .viewerBadge_link__qRIco,
    .viewerBadge_container {
        display: none !important;
    }

    .cover-badge {
        position: fixed;
        bottom: 0px;
        right: 0px;
        width: 100px;
        height: 100px;
        background-color: white;
        z-index: 9999;
    }
    </style>
    <script>
    document.addEventListener("DOMContentLoaded", function() {
        var badge = document.querySelector('.cover-badge');
        if (badge) {
            badge.style.zIndex = 9999;
        }
    });
    </script>
    <div class='cover-badge'></div>
"""
st.markdown(hide_button_script, unsafe_allow_html=True)

# Add input field
st.title('Enter Your Information')
user_input = st.text_input("Enter information here:")
st.write("The information you entered is:", user_input)

# باقي كود تطبيقك هنا
# ...
