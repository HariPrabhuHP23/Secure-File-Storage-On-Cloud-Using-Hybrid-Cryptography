import streamlit as st
import requests
from streamlit_lottie import st_lottie
import af_login
def main():
    #st.set_page_config(page_title="Upload")
    st.title("Secure File Storage")
    st.subheader("File Upload")
    #left,right=st.columns(2)
    #with left:
    with st.form("Upload"):
        reciv=st.selectbox(label="Select Your receiver",options=["harikrish0122001@gmail.com","hariprabhu2323@gmail.com","harishretinam@gmail.com"])
        upload=st.file_uploader("Select Your File",accept_multiple_files=1)
        key=st.text_input("Enter Key:")
        img=st.file_uploader("Select Image",type=[".jpg",'.png','.jpeg'])

        up_button=st.form_submit_button("Upload")

    if up_button:
        if not upload:
            st.error("Please Upload File")
        elif not key:
            st.error("Please enter Key")
        elif not img:
            st.error('Please Upload Image')
        else:
            st.success("File upload successfully!!!")
            af_login.main()

            '''
    #with right:
        def animation(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()


        streamlit_coding = animation("https://assets3.lottiefiles.com/packages/lf20_Hg1eiy.json")
        st_lottie(streamlit_coding, height=300, key="Coding1")
        '''
main()