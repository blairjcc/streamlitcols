import streamlit as st
import pandas as pd
import numpy as np

def foo():
	print('bar')


st.set_page_config(layout='wide')
st.title('Streamlit Column Test with modified standard theme')
left, center, right = st.cols([1, 3, 1])

with left:
	st.subheader('Widgets')
	st.button('Click me')
	st.checkbox('I agree')

with center:
	st.radio('Pick one', ['cats', 'dogs'])
	st.selectbox('Pick one', ['cats', 'dogs'])
	st.multiselect('Buy', ['milk', 'apples', 'potatoes'])

with right:
	st.slider('Pick a number', 0, 100,50)
	st.select_slider('Pick a size', ['S', 'M', 'L'])
	st.text_input('First name')
