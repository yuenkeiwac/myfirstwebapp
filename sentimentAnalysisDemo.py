import nltk
nltk.download('vader_lexicon')
from sentimentAnalysis import Prediction
from load_css import local_css
import streamlit as st
import numpy as np
import pandas as pd
import time

local_css("style.css")
    
st.header("Sentiment Analysis")

readme = st.checkbox("readme first")

if readme:

    st.write("""
        This is a web app demo using [streamlit](https://streamlit.io/) library. It is hosted on [heroku](https://www.heroku.com/). You may get the codes via [github](https://github.com/yuenkeiwac/myfirstwebapp/sentimentAnalysis.py)
        """)

option = st.sidebar.selectbox(
    'Language',
     ['English','Chinese'])

predict = Prediction()

text = st.empty() 
sentence = text.text_input('Enter a sentence', '')
if sentence != '':
    if option == 'English':
        score = predict.split_sentence(sentence)
    elif option == 'Chinese':
        score = predict.Compute_CHIWord_Sentiment(sentence)
    color, sentiment = predict.returnSentiment(score)
    t = "<div>"+ sentence + "<span class='" + color + "'>   " + sentiment+ "</span></div>"
    #sentence = text.text_input('Enter a sentence', '', key='2')
    st.markdown(t, unsafe_allow_html=True)
    
#t = "<div>Hello there my <span class='highlight blue'>name <span class='bold'>yo</span> </span> is <span class='highlight red'>Fanilo <span class='bold'>Name</span></span></div>"


