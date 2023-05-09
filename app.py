import streamlit as st


with st.sidebar:
    st.markdown("<div><img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjI0MDVkZjhmZDgzMTRkNzlhYTMyYjllMGY1OGM3ZmZjYjMzNjc0MyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PXM/UvPvsX9oMlMWs/giphy.gif' width = 200></h1></div>", unsafe_allow_html=True)
    st.title("English Machine")
    choice = st.radio("Choose Function", ["Translator", "Spelling"])
    st.info("This app can accelerate the learning process English learners")
