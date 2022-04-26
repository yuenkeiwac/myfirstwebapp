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
 
sentence = st.text_input('Enter a sentence', 'I feel good today')
score = split_sentence(sentence)

if (score < 0):
    color = 'highlight red'
    sentiment = 'Negative'
elif (score > 0):
    color = 'highlight green'
    sentiment = 'Positive'
else:
    color = 'highlight orange'
    sentiment = 'Neutral'

t = "<div>"+ sentence + "<span class=" + color + ">" + sentiment+ "</span></div>"
sentence = st.text_input('Enter a sentence', 'I feel good today')
#t = "<div>Hello there my <span class='highlight blue'>name <span class='bold'>yo</span> </span> is <span class='highlight red'>Fanilo <span class='bold'>Name</span></span></div>"

st.markdown(t, unsafe_allow_html=True)

    
