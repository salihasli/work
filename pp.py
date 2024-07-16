import streamlit as st

st.title("Enter (customer) informaiton ")

hello=st.text_input(" THE NAME  ")
phone=st.text_input(" phone number ")
city=st.selectbox("select city", ["بغداد", "البصرة","نينوى","الانبار","ديالى","كربلاء","بابل","واسط","صلاح الدين","القادسيه","ذي قار","المثنى","ميسان","السليمانية","دهوك","لاربي","كركوك","النجف","الموصل","حلبجة"])
region= st.text_input("enter the region")
more=st.text_area("type here for more information")
file=st.file_uploader("choice file if you want", type=["jpg","png","pdf","docx"])

if st.button("continue"):
    st.write("Name", hello)
    st.write("phone number",phone)
    st.write("city",city)
    st.write("region",region)
    st.write("more informiton",more)
if file is not None:
        st.write("File uploaded successfully.")
        if file.type in ["image/jpeg", "image/png"]:
            st.image(file, caption="Uploaded Image")