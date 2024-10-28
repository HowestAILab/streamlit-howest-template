import streamlit as st
import toml

# Read Streamlit TOML config
CONFIG: dict = toml.load('./.streamlit/config.toml')
THEME: dict = CONFIG.get('theme', {})

# Extract TOML variables
BASE = THEME.get("base", "light")
PRIMARY_COLOR = THEME.get("primaryColor", "#44c8f5")
BACKGROUND_COLOR = THEME.get("backgroundColor", "#FAFEFF")
SECONDARY_BACKGROUND_COLOR = THEME.get("secondaryBackgroundColor", "#e9f6fb")

# Derived colors
TOP_BAR_COLOR = PRIMARY_COLOR
HEADER_COLOR = SECONDARY_BACKGROUND_COLOR if BASE == "dark" else "#FFFFFF"
BORDER_COLOR = "#4E505F" if BASE == "dark" else "#D6D6D6"

# CSS Variables
CSS_VARIABLES = \
    f"""
  :root {{
    --custom-primary-color: {PRIMARY_COLOR} !important;
    --custom-top-bar-color: {TOP_BAR_COLOR} !important;
    --custom-background-color: {BACKGROUND_COLOR} !important;
    --custom-header-color: {HEADER_COLOR} !important;
    --custom-border-color: {BORDER_COLOR} !important;
  }}
"""


@st.cache_data
def get_font_style() -> str:
    """Read `font.css` and return it as an HTML string."""
    style = ""
    try:
        with open('./style/font.css') as css:
            style = css.read()
    finally:
        return f"<style>{style}</style>"


@st.cache_data
def get_custom_css() -> str:
    """Read `style.css` and return it as an HTML string."""
    style = ""
    try:
        with open('./style/style.css') as css:
            style = CSS_VARIABLES + css.read()
    finally:
        return f"<style>{style}</style>"


def apply():
    """Apply font styles and custom CSS."""
    st.markdown(get_font_style(), unsafe_allow_html=True)
    st.markdown(get_custom_css(), unsafe_allow_html=True)
