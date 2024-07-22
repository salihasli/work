import streamlit as st
import json
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# إخفاء أزرار GitHub وزر "Manage app"
st.markdown("""
    <style>
    .viewerBadge_container__1QSob, button[title="Manage app"], .stActionButton, #MainMenu, footer { display: none !important; visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# تحميل وتخزين البيانات
def load_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            return data if isinstance(data, list) else st.error("Data format in file is incorrect.") or []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        st.error(f"Error loading data: {e}")
        return []

def save_data(new_data):
    if isinstance(new_data, list):
        with open('data.json', 'w') as f:
            json.dump(new_data, f)
        st.success("Data saved successfully!")
    else:
        st.error("Invalid data format for saving.")

# تنسيق الطلبات باستخدام HTML و CSS
def format_order(data, index):
    formatted_number = "{:,.0f}".format(data.get('number', 0)).replace(',', '.')
    background_color = "#d4edda" if data.get('status') == 'Completed' else "#f8d7da"
    if data.get('status') == 'Delivered':
        background_color = "#cce5ff"
    status_color = "green" if data.get('status') == 'Completed' else "red"
    if data.get('status') == 'Delivered':
        status_color = "blue"
    return f"""
    <div style="border-radius: 8px; padding: 16px; margin-bottom: 10px; background-color: #fff; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <div style="display: flex; flex-direction: column; align-items: flex-start;">
            <div style="font-weight: bold; font-size: 1.2em;">{data.get('hello', 'N/A')}</div>
            <div style="color: gray;">{data.get('region', 'N/A')}</div>
            <div style="margin: 8px 0;">
                <span style="background-color: {background_color}; padding: 4px 8px; border-radius: 4px; color: {status_color};"><strong>{data.get('status', 'N/A')}</strong></span>
                <span style="background-color: #f0f0f0; padding: 4px 8px; border-radius: 4px; margin-left: 8px;">Order #: {index+1}</span>
            </div>
            <div style="color: gray;">{data.get('phone', 'N/A')}</div>
        </div>
    </div>
    """

def format_order_details(data):
    formatted_number = "{:,.0f}".format(data.get('number', 0)).replace(',', '.')
    return f"""
    <div style="border-radius: 8px; padding: 16px; background-color: #fff; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <p><strong>Name:</strong> {data.get('hello', 'N/A')}</p>
        <p><strong>Phone Number:</strong> {data.get('phone', 'N/A')}</p>
        <p><strong>City:</strong> {data.get('city', 'N/A')}</p>
        <p><strong>Region:</strong> {data.get('region', 'N/A')}</p>
        <p><strong>Price:</strong> {formatted_number}</p>
        <p><strong>Type:</strong> {data.get('kind', 'N/A')}</p>
        <p><strong>Total:</strong> {data.get('total', 'N/A')}</p>
        <p><strong>More Information:</strong> {data.get('more', 'N/A')}</p>
        <p><strong>Status:</strong> {data.get('status', 'N/A')}</p>
    </div>
    """

# تعريف الكود السري للتحقق
code = "صالح"

# طلب كود التسجيل
if "is_authenticated" not in st.session_state:
    st.session_state.is_authenticated = False

if not st.session_state.is_authenticated:
    if st.text_input("Type your code") == code:
        st.session_state.is_authenticated = True
        st.success("Login successful")
    else:
        st.warning("Please enter a valid code to proceed.")
        st.stop()

# عرض القائمة بعد التحقق
selected = option_menu(
    menu_title="Menu",
    options=["Home", "Orders", "Search", "Dashboard"],
    icons=["house", "clipboard", "search", "graph-up"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

if selected == "Home":
    hello, phone = st.text_input("THE NAME"), st.text_input("Phone Number")
    city = st.selectbox("Select City", ["بغداد", "البصرة", "نينوى", "الانبار", "ديالى", "كربلاء", "بابل", "واسط", "صلاح الدين", "القادسيه", "ذي قار", "المثنى", "ميسان", "السليمانية", "دهوك", "اربيل", "كركوك", "النجف", "الموصل", "حلبجة"])
    region, kind = st.text_input("Enter the Region"), st.selectbox("type of prodact", ["smart watch", "airtag"])
    number, total = st.number_input('price', min_value=0.0, max_value=500000.0, value=25000.0, step=5000.0, format='%0.0f'), st.number_input('total', min_value=0, max_value=100, value=1, step=1)
    more = st.text_area("Type here for more information")

    if st.button("Save Data"):
        if len(phone) != 11 or not phone.isdigit():
            st.error("The phone number must be exactly 11 digits.")
        else:
            new_data = {'hello': hello, 'phone': phone, 'city': city, 'region': region, 'more': more, 'number': number, 'kind': kind, 'total': total, 'status': 'Pending', 'date': datetime.today().strftime('%Y-%m-%d')}
            existing_data = load_data()
            existing_data.insert(0, new_data)
            save_data(existing_data)

elif selected == "Orders":
    all_data = load_data()
    updated_data = all_data.copy()

    for i, data in enumerate(updated_data):
        st.markdown(format_order(data, i), unsafe_allow_html=True)
        with st.expander(f"View Details for Order {i+1}"):
            st.markdown(format_order_details(data), unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 1, 1])
            if col1.button(f"Toggle Status {i+1}", key=f"toggle_button_{i}"):
                new_status = 'Pending' if data.get('status') == 'Completed' else 'Completed'
                updated_data[i]['status'] = new_status
                save_data(updated_data)
                st.experimental_rerun()
            if col2.button(f"Mark as Delivered {i+1}", key=f"deliver_button_{i}"):
                updated_data[i]['status'] = 'Delivered'
                save_data(updated_data)
                st.experimental_rerun()
            if col3.button(f"Delete Entry {i+1}", key=f"delete_button_{i}"):
                del updated_data[i]
                save_data(updated_data)
                st.experimental_rerun()
            st.write("---")

elif selected == "Search":
    st.title("Search")
    if "search_query" not in st.session_state:
        st.session_state.search_query = ""
    search_query = st.text_input("Search by phone number or name", key="search_input")
    col1, col2 = st.columns([1, 1])
    if col1.button("Search"):
        st.session_state.search_query = search_query.lower()
    if col2.button("Clear Search"):
        st.session_state.search_query = ""

    if st.session_state.search_query:
        filtered_data = [entry for entry in load_data() if st.session_state.search_query in entry.get('phone', '').lower() or st.session_state.search_query in entry.get('hello', '').lower()]
        if filtered_data:
            for i, data in enumerate(filtered_data):
                st.markdown(format_order(data, i), unsafe_allow_html=True)
                with st.expander(f"View Details for Order {i+1}"):
                    st.markdown(format_order_details(data), unsafe_allow_html=True)
                    col1, col2, col3 = st.columns([1, 1, 1])
                    if col1.button(f"Toggle Status {i+1}", key=f"toggle_button_search_{i}"):
                        new_status = 'Pending' if data.get('status') == 'Completed' else 'Completed'
                        filtered_data[i]['status'] = new_status
                        save_data(filtered_data)
                        st.experimental_rerun()
                    if col2.button(f"Mark as Delivered {i+1}", key=f"deliver_button_search_{i}"):
                        filtered_data[i]['status'] = 'Delivered'
                        save_data(filtered_data)
                        st.experimental_rerun()
                    if col3.button(f"Delete Entry {i+1}", key=f"delete_button_search_{i}"):
                        del filtered_data[i]
                        save_data(filtered_data)
                        st.experimental_rerun()
        else:
            st.write("No entries found with your search criteria.")

elif selected == "Dashboard":
    # وظيفة لرسم دائرة مع خلفية بيضاء
    def draw_circle(value, label, color="#1E90FF", max_value=100):
        percentage = min(100, max(0, (value / max_value) * 100))
        angle = (percentage / 100) * 360
        with st.container():
            st.markdown(f"""
            <div style="display: flex; flex-direction: column; align-items: center; background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                <svg viewBox="0 0 36 36" width="150" height="150">
                    <path d="M18 2.0845
                             a 15.9155 15.9155 0 0 1 0 31.831
                             a 15.9155 15.9155 0 0 1 0 -31.831"
                          fill="none"
                          stroke="#eeeeee"
                          stroke-width="4"
                          stroke-linecap="round"></path>
                    <path d="M18 2.0845
                             a 15.9155 15.9155 0 0 1 0 31.831"
                          fill="none"
                          stroke="{color}"
                          stroke-width="4"
                          stroke-linecap="round"
                          stroke-dasharray="{angle}, 100"></path>
                    <text x="18" y="20.35" font-size="8" text-anchor="middle" fill="#333">{value}</text>
                </svg>
                <div style="margin-top: 10px;">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    # تحليل البيانات
    def analyze_data(data):
        total_orders = len(data)
        pending_orders = sum(1 for item in data if item.get('status') == 'Pending')
        completed_orders = sum(1 for item in data if item.get('status') == 'Completed')
        delivered_orders = sum(1 for item in data if item.get('status') == 'Delivered')
        total_revenue = sum(item.get('number', 0) for item in data if item.get('status') == 'Delivered')
        orders_by_city = {}
        revenue_by_city = {}
        orders_by_date = {}
        revenue_by_date = {}

        for item in data:
            city = item.get('city', 'Unknown')
            date_str = item.get('date', 'Unknown')
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                date = 'Unknown'
            
            orders_by_city[city] = orders_by_city.get(city, 0) + 1
            revenue_by_city[city] = revenue_by_city.get(city, 0) + item.get('number', 0)
            if date != 'Unknown':
                orders_by_date[date] = orders_by_date.get(date, 0) + 1
                if item.get('status') in ['Pending', 'Completed', 'Delivered']:
                    revenue_by_date[date] = revenue_by_date.get(date, 0) + (item['number'] if item['status'] == 'Delivered' else 0)

        return total_orders, pending_orders, completed_orders, delivered_orders, total_revenue, orders_by_city, revenue_by_city, orders_by_date, revenue_by_date

    # تحميل وتحليل البيانات
    data = load_data()
    total_orders, pending_orders, completed_orders, delivered_orders, total_revenue, orders_by_city, revenue_by_city, orders_by_date, revenue_by_date = analyze_data(data)

    # تحويل البيانات إلى إطار بيانات بانداس
    df_orders = pd.DataFrame(list(orders_by_date.items()), columns=['Date', 'Orders'])
    df_orders['Date'] = pd.to_datetime(df_orders['Date'], format='%Y-%m-%d')
    df_orders = df_orders.sort_values('Date')

    df_revenue = pd.DataFrame(list(revenue_by_date.items()), columns=['Date', 'Revenue'])
    df_revenue['Date'] = pd.to_datetime(df_revenue['Date'], format='%Y-%m-%d')
    df_revenue = df_revenue.sort_values('Date')

    # واجهة المستخدم
    st.title("Dashboard: Order Analysis")

    # تحديد القيم القصوى لكل دائرة
    max_total_orders = 1500
    max_pending_completed_orders = 150
    max_delivered_orders = 1000
    max_pending_orders_orders = 150
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        draw_circle(total_orders, "الطلبات الكلية", max_value=max_total_orders)
    with col2:
        draw_circle(pending_orders, "عدد الطلبات", max_value=max_pending_orders_orders)
    with col3:
        draw_circle(completed_orders, "الطلبات المسجلة", max_value=max_pending_completed_orders)
    with col4:
        draw_circle(delivered_orders, "الطلبات المستلمة", max_value=max_delivered_orders)

    # عرض الإيرادات اليومية بطريقة احترافية باستخدام بطاقات متعددة الأعمدة داخل expander
    with st.expander("عرض الإيرادات اليومية"):
        st.markdown("## Daily Revenue")
        today = datetime.today().date()
        daily_revenue = {date: revenue for date, revenue in revenue_by_date.items() if date == today}
    
        if today not in daily_revenue:
            daily_revenue[today] = 0

        dates = list(daily_revenue.keys())
        revenues = list(daily_revenue.values())

        num_cols = 3
        rows = len(dates) // num_cols + (len(dates) % num_cols > 0)

        for row in range(rows):
            cols = st.columns(num_cols)
            for col_index in range(num_cols):
                index = row * num_cols + col_index
                if index < len(dates):
                    with cols[col_index]:
                        formatted_revenue = "{:,.0f}".format(revenues[index]).replace(',', '.')
                        st.markdown(f"""
                        <div style="display: flex; flex-direction: column; align-items: center; background-color: white; padding: 10px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); margin: 10px 0;">
                            <h4>{dates[index].strftime('%Y-%m-%d')}</h4>
                            <p style="font-size: 20px; color: #1E90FF;"><strong>{formatted_revenue} دينار عراقي</strong></p>
                        </div>
                        """, unsafe_allow_html=True)





    st.markdown("<hr style='border:10px solid #eee'>", unsafe_allow_html=True)

