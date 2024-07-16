import streamlit as st

# تهيئة حالة تسجيل الدخول
if 'is_authenticated' not in st.session_state:
    st.session_state.is_authenticated = False

# ملاحة القائمة الجانبية
menu = st.sidebar.selectbox("Menu", ["Customer Information", "Another Section"])


# اليوزر والرمز الصحيح
user = "admin"
pas = "132"

#ازرار الادخال واجهيه الي تضهر للمستخدم
if not st.session_state.is_authenticated:
    st.title("Login Page")
    qq = st.text_input("User Name")
    ww = st.text_input("Password", type="password")
    go = st.button("Login")

        #خانة تحقق من الكود
    if go:
            if qq == user and ww == pas:
                st.session_state.is_authenticated = True
                st.success("Login successful")
            else:
                st.error("Error: Incorrect user or password")

elif menu == "Customer Information":
        if st.session_state.is_authenticated:
            st.title("Enter Customer Information")
            hello = st.text_input("THE NAME")
            phone = st.text_input("Phone Number")
            city = st.selectbox("Select City", ["بغداد", "البصرة", "نينوى", "الانبار", "ديالى", "كربلاء", "بابل", "واسط", "صلاح الدين", "القادسيه", "ذي قار", "المثنى", "ميسان", "السليمانية", "دهوك", "لاربي", "كركوك", "النجف", "الموصل", "حلبجة"])
            region = st.text_input("Enter the Region")
            more = st.text_area("Type here for more information")
            file = st.file_uploader("Upload your photo", type=["png", "jpg", "jpeg"])
        if st.button("Continue"):
            st.write("Name:", hello)
            st.write("Phone Number:", phone)
            st.write("City:", city)
            st.write("Region:", region)
            st.write("More Information:", more)
            st.image(file, caption="Uploaded Image")    


elif menu == "Another Section":
    if st.session_state.is_authenticated:
        st.title("Another Section")
        st.write("More content here.")
    
