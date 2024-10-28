from streamlit_extras.stylable_container import stylable_container
from style import style
import streamlit as st

HOWEST_CONTAINER_CSS = \
    f"""{{
    outline: 2px solid {style.PRIMARY_COLOR};
    border-radius: 8px;
    padding: 16px;
    background-color: {style.HEADER_COLOR};
    box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.1);
}}"""

HOWEST_CONTAINER_SECONDARY_CSS = \
    f"""{{
    outline: 1px solid {style.BORDER_COLOR};
    border-radius: 8px;
    padding: 16px;
    background-color: {style.HEADER_COLOR};
    box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.1);
}}"""

HOWEST_FOOTER_CSS = \
    f"""{{
    height: 32px;
    position: relative;
    bottom: 0;
    margin-top: 64px;
    text-align: center;
}}"""


def howest_container_primary(key: str):
    """
    Renders a Howest-styled container.\\
    Will fall back to default Streamlit container in case something goes wrong.
    """
    try:
        return stylable_container(key=key, css_styles=HOWEST_CONTAINER_CSS)
    except:
        return st.container(key=key, border=True)


def howest_container_secondary(key: str):
    """
    Renders a Howest-styled container.\\
    Will fall back to default Streamlit container in case something goes wrong.
    """
    try:
        return stylable_container(key=key, css_styles=HOWEST_CONTAINER_SECONDARY_CSS)
    except:
        return st.container(key=key, border=True)


def powered_by_howest_footer(key: str, powered_by: str = "Howest"):
    """
    Renders a `Powered by Howest` footer.\\
    Will fall back to default Streamlit elements in case something goes wrong.
    """
    try:
        footer = stylable_container(key=key, css_styles=HOWEST_FOOTER_CSS)
        with footer:
            footer.caption(f"Powered by **{powered_by}**")
        return footer
    except:
        c = st.container(height=32, border=False)   # Padding top 32px
        c1, c2, c3 = st.columns([3, 2, 3])          # Text align center
        with c2:
            st.caption(f"Powered by **{powered_by}**")
