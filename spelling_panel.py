import streamlit as st
from word_scrapping import word_scrapping

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