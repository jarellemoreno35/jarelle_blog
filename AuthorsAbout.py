import base64
import streamlit as st
import plotly.express as px
from PIL import Image

def app():
    st.title("About the Author")

    # ---- LOAD ASSETS ----
    img_contact_form = Image.open("profile-pic3.png")


    # ---- AUTHOR'S BACKGROUND ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns([1,2])
        
        with right_column:
            st.header("AUTHOR'S PROFILE")
            st.write(
                """
                PERSONAL INFORMATION
                - Hi everyone, I am JARELLE ANN MARIZ C. MORENO,
                a college student studying in the SURIGAO DEL NORTE STATE UNIVERSITY.
                
                EDUCATIONAL BACKGROUND
                - Elementary: SABANG ELEMENTARY SCHOOL
                - Junior High School: SISTERS OF MARY SCHOOL-GIRLSTOWN, INC.
                - Senior High School: SISTERS OF MARY SCHOOL-GIRLSTOWN, INC.
                - College Education: SURIGAO DEL NORTE STATE UNIVERSITY
                """
            )
            
        with left_column:
            st.image(img_contact_form)

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
    background-image: url("data:image/png;base64,{img2}");
    background-position: left; 
    background-repeat: repeat;
    background-size: 100%;
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