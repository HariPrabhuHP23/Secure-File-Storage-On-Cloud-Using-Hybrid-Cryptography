import streamlit as st
import requests
from streamlit_lottie import st_lottie

def animation(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

streamlit_coding = animation("https://assets5.lottiefiles.com/packages/lf20_dn6rwtwl.json")

def create():
    st.title("SignUp")
    left,right=st.columns(2)
    with left:
        firstname=st.text_input("First Name")
        lastname = st.text_input("Last Name")
        Email = st.text_input("Enter your Mail Id")
        Phoneno=st.text_input("Contact No")
        password = st.text_input("Enter a new password",type='password')
        repassword=st.text_input("Retype your password",type='password')
        signin=st.button("Create New Account")
        if signin:
            if not (firstname or lastname or Email or Phoneno or password or repassword):
                st.error("Please fill the Neccessary details")
            else:
                if password==repassword:
                    st.success("Account Created Successfully!!!")
                else:
                    st.error("Password mismatch")
    with right:
        st_lottie(streamlit_coding, height=300, key="signup")
