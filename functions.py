import streamlit as st
from pathlib import Path


@st.cache
def read_markdown_file(markdown_file):
    """
    create intro text from markdown file
    """
    return Path(markdown_file).read_text()
