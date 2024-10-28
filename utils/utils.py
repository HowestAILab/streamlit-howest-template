import streamlit as st
from PIL import Image
import pandas as pd
import dotenv
from style import style


@st.cache_data
def load_env() -> None:
    """
    This function appends the variables stored in `.env` to your environment.\\
    You can read environment variables using `os.getenv(key=...)`
    """
    dotenv.load_dotenv(".env")


@st.cache_data
def file_to_df(file) -> pd.DataFrame:
    """Convert an uploaded file to a cached Pandas DataFrame."""
    try:
        extension = file.name.split(".")[-1].lower()
        match(extension):
            case "csv":
                return pd.read_csv(file)
            case "xlsx":
                return pd.read_excel(file)
            case "pkl":
                return pd.read_pickle(file)
            case "json":
                return pd.read_json(file)
            case _:
                st.error("Unsupported file format")
    except:
        st.error("Failed to convert file to DataFrame.")


@st.cache_data
def get_howest_logo() -> Image.Image:
    """Return cached Howest logo."""
    if style.BASE == "dark":
        return Image.open("assets/howest_dark_mode.png")
    return Image.open("assets/howest_light_mode.png")
