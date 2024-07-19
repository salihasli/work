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
        st.markdown("""
        <style>
        .form-container {
            background: #ffffff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            font-family: 'Arial', sans-serif;
            color: #333;
            margin-top: 20px;
        }
        .form-container h2 {
            text-align: center;
            color: #0073e6;
            font-size: 24px;
        }
        .form-container .input-container {
            margin-bottom: 15px;
        }
        .form-container .input-container label {
            font-weight: bold;
            display: block;
            margin-bottom: 5px;
        }
        .form-container .input-container input,
        .form-container .input-container select,
        .form-container .input-container textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
        }
        .form-container .btn-save {
            background: linear-gradient(90deg, #0073e6, #005bb5);
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            display: block;
            width: 100%;
            text-align: center;
            font-size: 16px;
            margin-top: 20px;
            transition: background 0.3s;
        }
        .form-container .btn-save:hover {
            background: linear-gradient(90deg, #005bb5, #0073e6);
        }
        .form-container .spinner {
            display: none;
            border: 4px solid rgba(0, 0, 0, 0.1);
            border-radius: 50%;
            border-top: 4px solid #3498db;
            width: 40px;
            height: 40px;
            animation: spin 2s linear infinite;
            margin: auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        st.markdown('<h2>Enter Customer Information</h2>', unsafe_allow_html=True)
        
        hello = st.text_input("THE NAME", key="name")
        phone = st.text_input("Phone Number", key="phone")
        city = st.selectbox("Select City", ["بغداد", "البصرة", "نينوى", "الانبار", "ديالى", "كربلاء", "بابل", "واسط", "صلاح الدين", "القادسيه", "ذي قار", "المثنى", "ميسان", "السليمانية", "دهوك", "اربيل", "كركوك", "النجف", "الموصل", "حلبجة"], key="city")
        region = st.text_input("Enter the Region", key="region")
        kind = st.selectbox("type of prodact", ["smart watch", "airtag"], key="kind")
        number = st.number_input('price', min_value=0.0, max_value=500000.0, value=25000.0, step=5000.0, format='%0.0f', key="price")
        total = st.number_input('total', min_value=0, max_value=100, value=1, step=1, key="total")
        more = st.text_area("Type here for more information", key="more")

        if st.button("Save Data", key="save"):
            with st.spinner("Saving data..."):
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

        st.markdown('</div>', unsafe_allow_html=True)

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
                    formatted_number = "{:,.0f}".format(data['number'])
                    background_color = "#d4edda" if data.get('status') == 'Completed' else "#f8d7da"

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
        st.title("Settings")
        # إضافة إعدادات مناسبة هنا بناءً على متطلبات التطبيق
else:
    st.warning("Please enter a valid code to proceed.")