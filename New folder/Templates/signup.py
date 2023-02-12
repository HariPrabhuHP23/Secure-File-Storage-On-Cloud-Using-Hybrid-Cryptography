import streamlit as st
import requests
from streamlit_lottie import st_lottie
import index

def animation(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

streamlit_coding = animation("https://assets5.lottiefiles.com/packages/lf20_dn6rwtwl.json")
st_lottie(streamlit_coding, height=300)

def create():
    st.title("SignUp")
    #left,right=st.columns(2)
    #with left:
    with st.form("Signup"):
        fname=st.text_input("First Name")
        lastname = st.text_input("Last Name")
        Email = st.text_input("Enter your Mail Id")
        Phoneno=st.text_input("Contact No")
        password = st.text_input("Enter a new password",type='password')
        repassword=st.text_input("Retype your password",type='password')
        signin=st.form_submit_button("Create New Account")
        if signin:
            if not fname:
                st.error("Please Enter your First Name")
            elif not  lastname :
                st.error("Please Enter Your Last Name")
            elif not  Email:
                st.error("Please Enter Your Mail ID")
            elif not Phoneno:
                st.error("Please Enter Your Contact NO")
            elif not password:
                st.error("Please Enter Your Password")
            elif not repassword:
                st.error("Please Please Renter Your Password")
            else:
                if password==repassword:
                    st.success("Account Created Successfully!!!")
                    st.progress(100)


                else:
                    st.error("Password mismatch")
    #with right:


#create()