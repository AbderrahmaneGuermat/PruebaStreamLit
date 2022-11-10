import streamlit as st
import pandas as pd
import numpy as np

st.title('TESTING')


st.text_input("Your name", key="name")

st.write("HELLO ",st.session_state.name,"!!!")

number = st.number_input('Insert a number',min_value=5)
st.write('The current number is ', number)


col1, col2, col3 = st.columns(3)

with col1:
   st.header("Image 1")
   st.image("Image1.jpg",use_column_width='always')

with col2:
   st.header("Image 2")
   st.image("Image2.jpg",use_column_width='always')

with col3:
   st.header("Image 3")
   st.image("Image3.jpeg",use_column_width='always')


imagee = st.select_slider(
    'Select an image',
    options=['Image 1', 'Image 2', 'Image 3'])
st.write('My favorite image is', imagee)



uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)