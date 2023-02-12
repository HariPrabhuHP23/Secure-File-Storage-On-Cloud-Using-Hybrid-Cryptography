import streamlit as st
import Upload
import download

def main():
    st.title("Welcome to Secure File Storage")


    opt=st.selectbox("Select Your Choice",['Upload',"Download"])
    if opt=='Upload':
        Upload.main()
    elif opt=='Download':
        download.main()