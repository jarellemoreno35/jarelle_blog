import json
import requests
import streamlit as st
from streamlit_option_menu import option_menu
import Home,AuthorsAbout, MyProjects, Contact
import plotly.express as px
from PIL import Image
from streamlit_lottie import st_lottie

#Lottie files: https://lottiefiles.com/

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func): 

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Blog of Jarelle',
                options=['Home', 'AuthorsAbout','MyProjects','Contact'],
                icons=['house-fill','person-circle','book', 'telephone'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'teal'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#BD1B1B"},}
                
                )

        if app == 'Home':
            Home.app() 
        if app == 'AuthorsAbout':
            AuthorsAbout.app()            
        if app == 'MyProjects':
            MyProjects.app()
        if app == 'Contact':
            Contact.app()       
             
    run()            
         

