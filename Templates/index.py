import streamlit as st
import Login
import signup
import requests
from streamlit_lottie import st_lottie

def main():
    st.title("Secure File Storage")
    choice=st.sidebar.radio("Select",['Login','Signup'])


    left,right=st.columns(2)
    #with left:

    with right:
        def animation(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        streamlit_coding = animation("https://assets1.lottiefiles.com/packages/lf20_zhADUdzV8b.json")
        st_lottie(streamlit_coding, height=300, key="Coding")

    #login=st.button("LOGIN")
    if choice=="Login":
        Login.login()



    #sup=st.button("CREATE NEW ACCOUNT")
    else:
        signup.create()

if __name__ == "__main__":
    main()