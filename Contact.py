import json
import requests
import base64
import streamlit as st
import plotly.express as px
from PIL import Image
from streamlit_lottie import st_lottie

def app():
    df = px.data.iris()

    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()


    img = get_img_as_base64("P1.jpg")
    img1 = get_img_as_base64("P2.jpg")
    img2 = get_img_as_base64("P3.jpg")
    img3 = get_img_as_base64("P4.jpg")
    img4 = get_img_as_base64("P5.jpg")



    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img4}");
    background-position: left; 
    background-repeat: repeat;
    background-size: 10%;
    background-attachment: fixed;
    }}
    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/png;base64,{img}");
    background-position: left; 
    background-repeat: no-repeat;
    background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.title("Contact Us") 
    
    # ---- LOAD ASSETS ----

    # ---- CONTACT ----
    cols, cols1 = st.columns(2)
    with cols:
        with st.container():
            st.write("---")
            st.header("KEEP IN TOUCH WITH ME!")
            st.write("##")
            st.write(
                " For more questions, please address your queries here:"
            )

            # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
            contact_form = """
            <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st.empty()

    with cols1:
        def load_lottiefile(filepath: str):
                    with open(filepath, "r") as f:
                        return json.load(f)


        def load_lottieurl(url: str):
                    r = requests.get(url)
                    if r.status_code != 200:
                        return None
                    return r.json()
                

        lottie_coding = load_lottiefile("web2.json")  # replace link to local lottie file
        lottie_hello = load_lottieurl("https://lottie.host/14383c25-e7e8-4d55-b5e9-4716e9b2137c/lH1UkDqIM4.json")

        st_lottie(
                    lottie_hello,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="low", # medium ; high
                    height=None,
                    width=None,
                    key=None,
            )