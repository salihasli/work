import streamlit as st
import json
from streamlit_option_menu import option_menu

# تعريف الكود السري للتحقق
code = "salih"  # يجب تعيين كود السر الخاص بك هنا

# طلب كود التسجيل
st.title("If you have a code, enter here:")
user_code = st.text_input("Type your code")

if user_code == code:
    is_authenticated = True
    st.success("Login successful")
else:
    is_authenticated = False

# إذا كان التحقق ناجحاً، عرض القائمة
if is_authenticated:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Profile", "Settings"],
        icons=["house", "person", "gear"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal"
    )

    if selected == "Home":
        st.title("Enter Customer Information")
        hello = st.text_input("THE NAME")
        phone = st.text_input("Phone Number")
        city = st.selectbox("Select City", ["بغداد", "البصرة", "نينوى", "الانبار", "ديالى", "كربلاء", "بابل", "واسط", "صلاح الدين", "القادسيه", "ذي قار", "المثنى", "ميسان", "السليمانية", "دهوك", "اربيل", "كركوك", "النجف", "الموصل", "حلبجة"])
        region = st.text_input("Enter the Region")
        more = st.text_area("Type here for more information")
        number = st.number_input('أدخل رقمك المفضل', min_value=0, max_value=500000, value=0, step=1)

        if st.button("Save Data"):
            new_data = {'hello': hello, 'phone': phone, 'city': city, 'region': region, 'more': more, 'number': number}
            try:
                with open('data.json', 'r') as f:
                    old_data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                old_data = []
            old_data.append(new_data)
            with open('data.json', 'w') as f:
                json.dump(old_data, f)
            st.success("Data saved successfully!")

    elif selected == "Profile":
        st.title("Profile Information")
        try:
            with open('data.json', 'r') as f:
                all_data = json.load(f)
                for data in all_data:
                    st.write("Name:", data['hello'])
                    st.write("Phone Number:", data['phone'])
                    st.write("City:", data['city'])
                    st.write("Region:", data['region'])
                    st.write("More Information:", data['more'])
                    st.write("Number here:", data.get('number', 'No data'))
                    st.write("---")
        except FileNotFoundError:
            st.error("No data found. Please enter customer information first.")

    elif selected == "Settings":
        st.write("Here you can change your settings.")
else:
    st.warning("Please enter a valid code to proceed.")