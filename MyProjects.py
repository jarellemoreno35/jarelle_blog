import base64
import streamlit as st
import plotly.express as px
from PIL import Image

def app():
    # ---- LOAD ASSETS ----
    img_contact_form2 = Image.open("food.png")
    img_contact_form3 = Image.open("boracay.png")
    img_contact_form4 = Image.open("culture1.png")
    img_lottie_animation = Image.open("boracay.png")


    # ---- PROJECTS ----
    with st.container():
        st.write("---")
        st.header("PRESENTED PROJECTS")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_contact_form3)
        with text_column:
            st.subheader("TOURIST SPOTS THAT WILL MAKE YOU AWE")
            st.write(
                """
                Tourism plays vital role in the economic development of one country.
                Here in the Philippine setting, there are so many tourist spots and destinations.
                Which in fact made the country famous for and keeps attacts tourist to come over.
                """
            )
            st.markdown("[Watch Video...](https://www.youtube.com/watch?v=ZjFzkhrqIZs)")
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_contact_form2)
        with text_column:
            st.subheader("FOODS IN THE PHILIPPINES IS A BIG DRAW")
            st.write(
                """
                Food is very vital in our body. In the Philippines, as culture and tourism is a hit, food is also a big draw.
                Food in here is diverse and unique mixing both Asian and European influences.
                """
            )
            st.markdown("[Watch Video...](https://www.youtube.com/watch?v=lw3_W5X1t54)")
        with text_column:
            st.write(
                "To find more about the FOODS in this magnificent country, please click the link below"
            )
            st.markdown("https://theplanetd.com/bes-filipino-food/")
            
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_contact_form4)
        with text_column:
            st.subheader("DIVERSE CULTURE IN THE PHILIPPINES")
            st.write(
                """
                All nations are diverse in culture, the uniques is its beauty. In the Philippines a variety of distinct magnificent 
                cultures and various has manifested. From the clothing, foods, dances and even values all across the different regions.
                """
            )
            st.markdown("[Watch Video...](https://www.youtube.com/watch?v=8QsOcIsnERM)")
        


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
    background-image: url("data:image/png;base64,{img3}");
    background-position: left; 
    background-size: 150%;
    background-repeat: no-repeat
    background-attachment: local;
    }}
    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/png;base64,{img}");
    background-position: left; 
    background-size: 180%;
    background-repeat: no-repeat
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