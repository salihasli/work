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
        bottom: 0px;  /* التأكد من أن الطبقة تغطي الزر */
        right: 0px;   /* التأكد من أن الطبقة تغطي الزر */
        width: 100px;  /* زيادة العرض لتغطية الزر بالكامل */
        height: 100px; /* زيادة الارتفاع لتغطية الزر بالكامل */
        background-color: white;
        z-index: 9999;
    }
    </style>
    <div class='cover-badge'></div>
"""
st.markdown(hide_button_script, unsafe_allow_html=True)

# Add input field
st.title('Enter Your Information')
user_input = st.text_input("Enter information here:")
st.write("The information you entered is:", user_input)

# باقي كود تطبيقك هنا
# ...
