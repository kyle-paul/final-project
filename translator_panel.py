import streamlit as st
import pdf2image
from googletrans import Translator
import pytesseract

def translator():
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