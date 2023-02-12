import  streamlit as st
from streamlit_lottie import st_lottie
import  requests

#st.set_page_config(page_title="Download")
def main():
    st.title("Secure File Storage")
    st.subheader("Download")

    left,right=st.columns(2)
    with left:
        with st.form("Download"):
            av_files=st.selectbox(label='availabe',options=["hk.pdf","saala.img"])
            up_img=st.file_uploader("Upload image")
            st.form_submit_button("Download")
    with right:
        def animation(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()


        streamlit_coding = animation("https://assets4.lottiefiles.com/packages/lf20_szdrhwiq.json")
        st_lottie(streamlit_coding, height=300, key="Coding1")
