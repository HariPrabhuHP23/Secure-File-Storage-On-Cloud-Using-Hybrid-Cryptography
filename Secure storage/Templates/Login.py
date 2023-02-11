import streamlit as st
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Login")


def animation(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def login():

    st.title("User Login")
    st.write("LOGIN PAGE")

    left,right=st.columns(2)
    with left:
        username=st.text_input("User name")
        password=st.text_input("Password",type="password")
        sucess=st.button("Login")
        if sucess:
            if not(username or password):
                st.error("Please Enter Correct Username and Password")
            else:
                st.success("Login Successful !!!!")
                #sucessanimation=animation("https://assets1.lottiefiles.com/packages/lf20_7GoiCvHm8v.json")
                #st_lottie(sucessanimation,height=500,key="Success")



    with right:
        streamlit_coding = animation("https://assets3.lottiefiles.com/packages/lf20_Hg1eiy.json")
        st_lottie(streamlit_coding, height=300, key="Coding1")



