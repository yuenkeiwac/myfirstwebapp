import streamlit as st

import numpy as np
import pandas as pd
import time

st.header("Chart")

readme = st.checkbox("readme first")

if readme:

    st.write("""
        This is a web app demo using [streamlit](https://streamlit.io/) library. It is hosted on [heroku](https://www.heroku.com/). You may get the codes via [github](https://github.com/yuenkeiwac/myfirstwebapp)
        """)

    st.write ("For more info, please contact:")

    st.write("<a href='https://www.linkedin.com/in/khor-yuen-kei-5505441b7/'>Khor Yuen Kei </a>", unsafe_allow_html=True)

option = st.sidebar.selectbox(
    'Select a mini project',
     ['area chart', 'line chart', 'bar chart', 'map', 'color picker', 'T n C','Long Process'])


if option=='line chart':
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

elif option=='area chart':
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
    st.area_chart(chart_data)

elif option=='bar chart':
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])
    st.bar_chart(chart_data)
 
elif option=='map':
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(map_data)

elif option=='color picker':
    color = st.color_picker('Pick A Color', '#00f900')
    st.write('The current color is', color)
    
elif option=='T n C':

    st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
    show = st.checkbox('I agree the terms and conditions')
    if show:
        st.write(pd.DataFrame({
        'Intplan': ['yes', 'yes', 'yes', 'no'],
        'Churn Status': [0, 0, 0, 1]
        }))


else:
    'Starting a long computation...'

    
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
   
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'
