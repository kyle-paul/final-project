import streamlit as st
import pdf2image
from googletrans import Translator
import pytesseract


# Create sidebar
with st.sidebar:
    st.markdown("<div><img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjI0MDVkZjhmZDgzMTRkNzlhYTMyYjllMGY1OGM3ZmZjYjMzNjc0MyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PXM/UvPvsX9oMlMWs/giphy.gif' width = 200></h1></div>", unsafe_allow_html=True)
    st.title("English Machine")
    choice = st.radio("Choose Function", ["Translator", "Spelling"])
    st.info("This app can accelerate the learning process English learners")


# Function 1: Translator
if choice == "Translator":
    st.title("Page Translator")
    pdf_file = st.file_uploader("Choose a pdf file", type=["pdf"])

    if pdf_file is not None:
        poppler_path = r"C:\poppler-0.68.0\bin"
        images = pdf2image.convert_from_bytes(pdf_file.read(), poppler_path=poppler_path)
        
        translator = Translator() 
        
        for i, image in enumerate(images):
            col1, col2 = st.columns(2)
            
            with col1:
                st.image(image, caption=f"Page {i+1}")

            with col2:
                myconfig = r"--psm 6 --oem 3"
                text = pytesseract.image_to_string(image, config=myconfig, lang='deu')
                translation = translator.translate(text, src='en', dest='vi') 
                st.write(translation.text) 
            st.write('---')