import streamlit as st

st.title("Enter (customer) informaiton ")

hello=st.text_input(" THE NAME  ")
phone=st.text_input(" phone number ")
if not phone.isdigit():
    st.write("enter only number")
city=st.selectbox("select city", ["بغداد", "البصرة","نينوى","الانبار","ديالى","كربلاء","بابل","واسط","صلاح الدين","القادسيه","ذي قار","المثنى","ميسان","السليمانية","دهوك","لاربي","كركوك","النجف","الموصل","حلبجة"])
region= st.text_input("enter the region")
more=st.text_area("type here for more information")
file=st.file_uploader("choice file if you want", type=["jpg","png","pdf","docx"])