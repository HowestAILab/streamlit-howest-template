from utils.utils import load_env, get_howest_logo, file_to_df
from components.components import howest_container_primary, howest_container_secondary, powered_by_howest_footer
from style import style
import streamlit as st
from PIL import Image
import pandas as pd


# Page configuration
st.set_page_config("Howest", Image.open("assets/favicon.ico"))
style.apply()
load_env()


# Define each *independent* section of your page in a fragment function

@st.fragment
def section1():
    st.logo(get_howest_logo(), size="large", link="https://www.howest.be/")
    st.markdown('## This is a section')
    hc = howest_container_primary('section1')
    with hc:
        st.write('This is a Howest-styled container.')
        # Put your page elements here
        # ...


@st.fragment
def section2():
    st.logo(get_howest_logo(), size="large", link="https://www.howest.be/")
    st.markdown('## Another section')
    hc = howest_container_secondary('section2')
    with hc:
        st.write('This is a Howest-styled container.')
        # Put your page elements here
        # ...


# Render the page
st.title('Howest template')
section1()
section2()
powered_by_howest_footer(key="powered_by_howest_footer")
