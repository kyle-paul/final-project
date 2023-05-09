import random
import nltk
from wordhoard import Synonyms
import streamlit as st

@st.cache_data
def word_scrapping():
    # Get the list of words
    nltk.download('brown')
    word_list = nltk.corpus.brown.words()
    short_words = [w for w in word_list if len(w) <= 12 and len(w) >= 7]
    freq_dist = nltk.FreqDist(w.lower() for w in short_words)
    common_words = [w for w, f in freq_dist.most_common(1000)]
    random_word = random.choice(common_words)

    # get synnonyms
    synonym = Synonyms(search_string=random_word)
    synonym_results = synonym.find_synonyms()
    return synonym_results, random_word