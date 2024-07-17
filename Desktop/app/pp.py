import streamlit as st
import json
from streamlit_option_menu import option_menu

# تهيئة حالة تسجيل الدخول
if 'is_authenticated' not in st.session_state:
    st.session_state.is_authenticated = False

code = "''"

if not st.session_state.is_authenticated:
    st.title("if you have code enter here")
    qq = st.text_input("type your code")
    ww = st.button("submit")

    if ww:
        if qq == code:
            st.session_state.is_authenticated = True
            st.success("Login successful")

if st.session_state.is_authenticated:
    # إضافة شريط التنقل
    selected = option_menu(
        menu_title="here is,",
        options=["Home", "Profile", "Settings"],
        icons=["house", "person", "gear"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

    # عرض المحتوى حسب الاختيار من شريط التنقل
    if selected == "Home":
        st.title("Enter Customer Information")
        hello = st.text_input("THE NAME")
        phone = st.text_input("Phone Number")
        city = st.selectbox("Select City", ["بغداد", "البصرة", "نينوى", "الانبار", "ديالى", "كربلاء", "بابل", "واسط", "صلاح الدين", "القادسيه", "ذي قار", "المثنى", "ميسان", "السليمانية", "دهوك", "اربيل", "كركوك", "النجف", "الموصل", "حلبجة"])
        region = st.text_input("Enter the Region")
        more = st.text_area("Type here for more information")
        file = st.file_uploader("Upload your photo", type=["png", "jpg", "jpeg"])

        if st.button("Continue"):
            st.session_state['hello'] = hello
            st.session_state['phone'] = phone
            st.session_state['city'] = city
            st.session_state['region'] = region
            st.session_state['more'] = more
            st.session_state['file'] = file
            st.session_state['show_image'] = False

            # قراءة البيانات القديمة
            try:
                with open('data.json', 'r') as f:
                    old_data = json.load(f)
                    if not isinstance(old_data, list):
                        old_data = []
            except (FileNotFoundError, json.JSONDecodeError):
                old_data = []

            # إضافة البيانات الجديدة
            new_data = {
                'hello': hello,
                'phone': phone,
                'city': city,
                'region': region,
                'more': more,
                'file': file.name if file is not None else None
            }

            old_data.append(new_data)

            # حفظ البيانات المحدثة في ملف JSON
            with open('data.json', 'w') as f:
                json.dump(old_data, f)

            # حفظ الملف إذا كان موجودًا
            if file is not None:
                with open(file.name, 'wb') as f:
                    f.write(file.getbuffer())

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

                    if data['file']:
                        st.write("This is the uploaded image:")
                        # استعادة وعرض الملف
                        try:
                            with open(data['file'], 'rb') as f:
                                st.image(f.read(), caption="Uploaded Image")
                        except FileNotFoundError:
                            st.write("Image file not found.")
                    else:
                        st.write("No image uploaded.")
                    st.write("---")
        except FileNotFoundError:
            st.write("No data found. Please enter customer information first.")

    elif selected == "Settings":
        st.write("Here you can change your settings.")
