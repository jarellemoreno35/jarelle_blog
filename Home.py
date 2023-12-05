import base64
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import plotly.express as px

def app():   
    # ---- HEADER SECTION ----
    with st.container():
        st.title("MAIN PAGE")
        st.subheader("WELCOME TO THE PHILIPPINES 😉")
        st.title("Also known as Gems of the East. Moreover, named to be Orphans of the Pacific and Land of the Morning.")
        st.write(
            "Let's emerged to the beauty of the Land of the Morning the PHILIPPINES"
        )
        st.write("[Learn More >](https://www.youtube.com/watch?v=nQvoTSHV13A)")

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
    background-image: url("data:image/png;base64,{img1}");
    background-position: left; 
    background-repeat: no-repeat;
    background-size: 150%;
    background-attachment: local;
    }}
    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/png;base64,{img}");
    background-position: left; 
    background-repeat: no-repeat;
    background-size: 180%;
    background-attachment: local;
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