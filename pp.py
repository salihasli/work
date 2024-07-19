import streamlit as st
import json
from streamlit_option_menu import option_menu
import os

# تعريف الكود السري للتحقق
code = "صالح"  # يجب تعيين كود السر الخاص بك هنا

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
        kind = st.selectbox("type of prodact", ["smart watch", "airtag"])
        number = st.number_input('price', min_value=0.0, max_value=500000.0, value=25000.0, step=5000.0, format='%0.0f')
        formatted_number = "{:,.0f}".format(number)
        total = st.number_input('total', min_value=0, max_value=100, value=1, step=1)
        more = st.text_area("Type here for more information")

        if st.button("Save Data"):
            new_data = {'hello': hello, 'phone': phone, 'city': city, 'region': region, 'more': more, 'number': number, 'kind': kind, 'total': total, 'status': 'Pending'}
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
                try:
                    all_data = json.load(f)
                except json.JSONDecodeError:
                    all_data = []

                delete_index = st.session_state.get('delete_index', -1)
                if delete_index >= 0 and delete_index < len(all_data):
                    del all_data[delete_index]
                    with open('data.json', 'w') as f:
                        json.dump(all_data, f)
                    st.success(f"Entry {delete_index + 1} deleted successfully!")
                    st.session_state.delete_index = -1
                    st.experimental_rerun()

                for i, data in enumerate(all_data):
                    # Calculate formatted_number inside the loop
                    formatted_number = "{:,.0f}".format(data['number'])

                    # Determine the background color based on the status
                    background_color = "#d4edda" if data.get('status') == 'Completed' else "#f8d7da"

                    # Create a container with the appropriate background color and animation
                    st.markdown(
                        f"""
                        <div style="border: 2px solid gray; padding: 10px; margin-bottom: 10px; background-color: {background_color}; border-radius: 5px; transition: background-color 0.5s ease;">
                            <p><strong>Name:</strong> {data['hello']}</p>
                            <p><strong>Phone Number:</strong> {data['phone']}</p>
                            <p><strong>City:</strong> {data['city']}</p>
                            <p><strong>Region:</strong> {data['region']}</p>
                            <p><strong>Price:</strong> {formatted_number}</p>
                            <p><strong>Type:</strong> {data['kind']}</p>
                            <p><strong>Total:</strong> {data.get('total')}</p>
                            <p><strong>More Information:</strong> {data['more']}</p>
                            {"<p style='color: green;'><strong>Status:</strong> &#x2714; Completed</p>" if data.get('status') == 'Completed' else ""}
                        </div>
                        """, unsafe_allow_html=True
                    )

                    if st.button(f"Toggle Status {i+1}", key=f"toggle_button_{i}"):
                        new_status = 'Pending' if data.get('status') == 'Completed' else 'Completed'
                        all_data[i]['status'] = new_status
                        with open('data.json', 'w') as f:
                            json.dump(all_data, f)
                        st.success(f"Entry {i+1} status changed to {new_status}!")
                        st.experimental_rerun()

                    if st.button(f"Delete Entry {i+1}", key=f"delete_button_{i}"):
                        st.session_state.delete_index = i
                        st.experimental_rerun()
                    st.write("---")
        except FileNotFoundError:
            st.error("No data found. Please enter customer information first.")

    elif selected == "Settings":
        st.write("Here you can change your settings.")
else:
    st.warning("Please enter a valid code to proceed.")