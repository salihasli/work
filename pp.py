import streamlit as st

# اليوزر والرمز الصحيح
user = "admin"
pas = "132"

# تهيئة حالة تسجيل الدخول
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# صفحة الدخول
if not st.session_state.logged_in:
    st.title("Login Page")
    qq = st.text_input("User Name")
    ww = st.text_input("Password", type="password")
    go = st.button("Login")

    if go:
        if qq == user and ww == pas:
            st.session_state.logged_in = True  # تحديث حالة تسجيل الدخول
            st.experimental_rerun()  # إعادة تحميل الصفحة
        else:
            st.error("Error: Incorrect user or password")

# صفحة المعلومات بعد تسجيل الدخول
if st.session_state.logged_in:
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

    if file:
        st.image(file, caption="Uploaded Image")