import streamlit as st

import numpy as np
import pandas as pd
import time

st.header("Sentiment Analysis")

readme = st.checkbox("readme first")

if readme:

    st.write("""
        This is a web app demo using [streamlit](https://streamlit.io/) library. It is hosted on [heroku](https://www.heroku.com/). You may get the codes via [github](https://github.com/yuenkeiwac/myfirstwebapp/sentimentAnalysis.py)
        """)
 
title = st.text_input('Enter a sentence', 'Life of Brian')
