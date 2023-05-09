import streamlit as st
from sidebar import create_sidebar
from translator_panel import translator
from spelling_panel import create_dictionary_function
from keras.models import load_model, create_canvas, check

# load model
model = load_model('CNN_model.h5')

# Create sidebar
with st.sidebar:
    choice = create_sidebar()

# Panel 1: Translator
if choice == "Translator":
    translator()
            
# Panel 2: Spelling
if choice == "spelling":
    st.title("Enhance your spelling")
    selected_word = create_dictionary_function()
    result_str = create_canvas(model)
    check(result_str, selected_word)
    
    