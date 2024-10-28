from components.components import howest_container_primary, howest_container_secondary, powered_by_howest_footer
from utils.utils import load_env, get_howest_logo, file_to_df
from style import style
import streamlit as st
from PIL import Image
import pandas as pd
import time

# Page configuration
st.set_page_config("Howest", Image.open("assets/favicon.ico"))
style.apply()
load_env()

# Page design starts from this point
st.logo(get_howest_logo(), size="large", link="https://www.howest.be/")
st.title('Howest template')


# ========================================================================================


st.markdown('## Buttons')
c1, c2 = st.columns(2)
with c1:
    clicked = st.button("Primary button", type="primary",
                        disabled=False, use_container_width=True)
    if clicked:
        st.balloons()
with c2:
    clicked = st.button("Secondary button", type="secondary",
                        disabled=False, use_container_width=True)
    if clicked:
        st.toast("Secondary button clicked.")


# ========================================================================================


st.markdown('## Containers')
c1, c2 = st.columns(2)
with c1:
    hc = howest_container_primary("custom_container1")
    with hc:
        st.write("Primary Howest-styled container.")
with c2:
    hcs = howest_container_secondary("custom_container2")
    with hcs:
        st.write("Secondary Howest-styled container.")


# ========================================================================================


st.markdown('## Inputs')
c1, c2 = st.columns(2)
with c1:
    text = st.text_input("Enter text", placeholder="Some text here")
with c2:
    date = st.date_input("Select date", value="today")

c1, c2 = st.columns(2)
with c1:
    number = st.number_input(
        "Pick a number", min_value=0, max_value=10, step=1)
with c2:
    option = st.selectbox("Select an option", options=["Option 1", "Option 2"])

st.slider("Slider", min_value=0, max_value=10, step=1, value=5)

c1, c2, c3 = st.columns(3)
with c1:
    option: str = st.radio(
        "Radio", options=["Radio 1", "Radio 2"], label_visibility="collapsed")
with c2:
    checked: bool = st.checkbox("Checkbox")
with c3:
    state: bool = st.toggle("Toggle")


# ========================================================================================


st.markdown('## Callouts')
st.info("This is some information.", icon=":material/info:")
st.warning("This is a warning.", icon="⚠️")
st.error("This is an error.", icon="⛔")


# ========================================================================================


st.markdown('## File upload')
file = st.file_uploader("Upload a file", type=["csv", "xlsx", "pkl", "json"])
if file is not None:
    df = file_to_df(file)
    st.markdown(f"**Filename:** {file.name}")
    st.markdown(f"**Columns:** {list(df.columns)}")


# ========================================================================================


st.markdown('## Progress indicators')
clicked = st.button("Click me")
if clicked:
    p = st.progress(0, text="Progress bar")
    s = st.status("Processing...", expanded=True, state="running")
    time.sleep(1)
    for i in range(1, 5):
        precentage = round((i / 4) * 100)
        p.progress(i / 4, text=f"Progress {precentage}%")
        s.write(f"Status update {i}")
        time.sleep(1)
    s.update(label="Done processing", state="complete")


# ========================================================================================


powered_by_howest_footer(key="powered_by_howest_footer")
