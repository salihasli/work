import streamlit as st
import json
import requests
from streamlit_option_menu import option_menu
import os

# إخفاء زر GitHub وزر "Manage app"
hide_buttons_style = """
    <style>
    .viewerBadge_container__1QSob { 
        display: none !important; 
    }
    #MainMenu {
        visibility: hidden;
    }
    footer {
        visibility: hidden;
    }
    </style>
"""
st.markdown(hide_buttons_style, unsafe_allow_html=True)

# استخدم الرمز المميز المخزن في المتغير البيئي
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# إعدادات الطلب للوصول إلى المستودع الخاص
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3.raw"
}

# URL لملف JSON في المستودع الخاص
repo_owner = "salihasli"
repo_name = "work"
path_to_file = "data.json"
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{path_to_file}"

# تحميل البيانات من المستودع الخاص
def load_data():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.json()['content'].decode('utf-8'))
    else:
        return []

# تخزين البيانات الجديدة في الملف
def save_data(new_data):
    old_data = load_data()
    old_data.insert(0, new_data)
    data_content = json.dumps(old_data).encode('utf-8').decode('ascii')
    get_sha_response = requests.get(url, headers=headers)
    if get_sha_response.status_code == 200:
        sha = get_sha_response.json()['sha']
        payload = {
            "message": "update data",
            "content": data_content,
            "sha": sha
        }
        response = requests.put(url, headers=headers, json=payload)
        if response.status_code == 200 or response.status_code == 201:
            st.success("Data saved successfully!")
        else:
            st.error("Failed to save data.")
    else:
        st.error("Failed to get file sha.")

# تنسيق الطلبات باستخدام HTML و CSS
def format_order(data, index):
    formatted_number = "{:,.0f}".format(data['number'])
    background_color = "#d4edda" if data.get('status') == 'Completed' else "#f8d7da"
    status_color = "green" if data.get('status') == 'Completed' else "red"
    order_html = f"""
    <div style="border-radius: 8px; padding: 16px; margin-bottom: 10px; background-color: #fff; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <div style="display: flex; flex-direction: column; align-items: flex-start;">
            <div style="font-weight: bold; font-size: 1.2em;">{data['hello']}</div>
            <div style="color: gray;">{data['region']}</div>
            <div style="margin: 8px 0;">
                <span style="background-color: {background_color}; padding: 4px 8px; border-radius: 4px; color: {status_color};"><strong>{data.get('status')}</strong></span>
                <span style="background-color: #f0f0f0; padding: 4px 8px; border-radius: 4px; margin-left: 8px;">Order #: {index+1}</span>
            </div>
            <div style="color: gray;">{data['phone']}</div>
        </div>
    </div>
    """
    return order_html

def format_order_details(data):
    details_html = f"""
    <div style="border-radius: 8px; padding: 16px; background-color: #fff; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <p><strong>Name:</strong> {data['hello']}</p>
        <p><strong>Phone Number:</strong> {data['phone']}</p>
        <p><strong>City:</strong> {data['city']}</p>
        <p><strong>Region:</strong> {data['region']}</p>
        <p><strong>Price:</strong> {data['number']}</p>
        <p><strong>Type:</strong> {data['kind']}</p>
        <p><strong>Total:</strong> {data['total']}</p>
        <p><strong>More Information:</strong> {data['more']}</p>
        <p><strong>Status:</strong> {data['status']}</p>
    </div>
    """
    return details_html

# تعريف الكود السري للتحقق
code = "صالح"  # يجب تعيين كود السر الخاص بك هنا

# طلب كود التسجيل
st.title("If you have a code, enter here:")
user_code = st.text_input("Type your code")

is_authenticated = False
if user_code == code:
    is_authenticated = True
    st.success("Login successful")
else:
    st.warning("Please enter a valid code to proceed.")

# إذا كان التحقق ناجحاً، عرض القائمة
if is_authenticated:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Orders", "Search"],
        icons=["house", "clipboard", "search"],
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
        total = st.number_input('total', min_value=0, max_value=100, value=1, step=1)
        more = st.text_area("Type here for more information")

        if st.button("Save Data"):
            new_data = {'hello': hello, 'phone': phone, 'city': city, 'region': region, 'more': more, 'number': number, 'kind': kind, 'total': total, 'status': 'Pending'}
            save_data(new_data)

    elif selected == "Orders":
        st.title("Order Information")

        all_data = load_data()

        for i, data in enumerate(all_data):
            st.markdown(format_order(data, i), unsafe_allow_html=True)
            with st.expander(f"View Details for Order {i+1}"):
                st.markdown(format_order_details(data), unsafe_allow_html=True)
                col1, col2 = st.columns([1, 1])
                if col1.button(f"Toggle Status {i+1}", key=f"toggle_button_{i}"):
                    new_status = 'Pending' if data.get('status') == 'Completed' else 'Completed'
                    all_data[i]['status'] = new_status
                    save_data(all_data)
                    st.experimental_rerun()
                if col2.button(f"Delete Entry {i+1}", key=f"delete_button_{i}"):
                    del all_data[i]
                    save_data(all_data)
                    st.experimental_rerun()
                st.write("---")

    elif selected == "Search":
        st.title("Search")

        if "search_query" not in st.session_state:
            st.session_state.search_query = ""

        search_query = st.text_input("Search by phone number or name", key="search_input")

        col1, col2 = st.columns([1, 1])
        with col1:
            search_button = st.button("Search")
        with col2:
            clear_button = st.button("Clear Search")

        if search_button:
            st.session_state.search_query = search_query
        elif clear_button:
            st.session_state.search_query = ""
            st.experimental_rerun()

        all_data = load_data()

        # تطبيق الفلترة
        filtered_data = [entry for entry in all_data if st.session_state.search_query.lower() in entry['phone'].lower() or st.session_state.search_query.lower() in entry['hello'].lower()]

        for i, data in enumerate(filtered_data):
            st.markdown(format_order(data, i), unsafe_allow_html=True)
            with st.expander(f"View Details for Order {i+1}"):
                st.markdown(format_order_details(data), unsafe_allow_html=True)
                col1, col2 = st.columns([1, 1])
                if col1.button(f"Toggle Status {i+1}", key=f"toggle_button_search_{i}"):
                    new_status = 'Pending' if data.get('status') == 'Completed' else 'Completed'
                    filtered_data[i]['status'] = new_status
                    save_data(filtered_data)
                    st.experimental_rerun()
                if col2.button(f"Delete Entry {i+1}", key=f"delete_button_search_{i}"):
                    del filtered_data[i]
                    save_data(filtered_data)
                    st.experimental_rerun()
                st.write("---")
