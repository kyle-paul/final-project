import streamlit as st
from sidebar import create_sidebar
from translator_panel import translator

# Create sidebar
with st.sidebar:
    choice = create_sidebar()

# Panel 1: Translator
if choice == "Translator":
    translator()
            
