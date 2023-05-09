import streamlit as st
from word_scrapping import word_scrapping
import numpy as np
from streamlit_drawable_canvas import st_canvas
import cv2
import skimage.transform
from googletrans import Translator 


def create_dictionary_function():
    if "score" not in st.session_state:
        st.session_state["score"] = 10
    if "count" not in st.session_state:
        st.session_state["count"] = 0
    
    synonym_list, selected_word = word_scrapping()
    if st.button('Random word now'):
        st.write(f'The length of the word is {len(selected_word)}')
        st.write('relevant word:', synonym_list[st.session_state["count"]])
    
    
    if st.button('Reveal more relevant words'):
        st.session_state["count"] = st.session_state["count"] + 1
        st.write(synonym_list[st.session_state["count"]])
    
    if st.button('Reveal the word now'):
        st.write(selected_word)
        st.session_state["score"] = 0
        st.session_state["count"] = 0
    
    score = int(st.session_state["score"])
    count = int(st.session_state["count"])
    st.info(f"Your current score: {score - count} points")
    
    return selected_word
    
def create_canvas(model):
    stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 10)
    realtime_update = st.sidebar.checkbox("Update in realtime", True)

    result_str = ""
    num_cols = st.number_input ('Enter the number of the word length', min_value=7, max_value=12, value=8, step=1)
    cols = st.columns(num_cols)
    
    for i, col in enumerate (cols):
        # Create a canvas component
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",  
            stroke_width=stroke_width,
            stroke_color="#ffffff",
            background_color= "#000000",
            update_streamlit=realtime_update,
            drawing_mode="freedraw",
            height=150,
            width=150,
            key="canvas" + str(i),
        )
        if canvas_result.image_data is not None:
            gray = cv2.cvtColor(canvas_result.image_data, cv2.COLOR_BGR2GRAY)
            resized = skimage.transform.resize(gray, output_shape=(28, 28))
            input = resized.reshape((1,28,28,1))
            prediction = model.predict(input)
            label = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
            st.write(label[np.argmax(prediction)])
            result_str += label[np.argmax(prediction)]
            
    return result_str
            
def check(result_str, selected_word):
    st.info(result_str)
    translator = Translator() 
    translation = translator.translate(result_str, src='en', dest='vi') 
    st.info(translation.text) 
    if selected_word == result_str.lower():
        st.success("Correct")
    else:
        st.error("Incorrect")