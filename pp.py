import streamlit as st

# Hide the Streamlit hosted button using CSS and JavaScript
hide_button_script = """
    <style>
    .cover-badge {
        position: fixed;
        bottom: 0;
        right: 0;
        width: 80px;  /* زيادة العرض لتغطية الزر بالكامل */
        height: 80px;  /* زيادة الارتفاع لتغطية الزر بالكامل */
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
