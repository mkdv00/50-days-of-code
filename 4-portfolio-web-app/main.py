from content import description
import streamlit as st
import pandas

st.set_page_config(layout='wide')

col_1, col_2 = st.columns(2)

with col_1:
    st.image('images\photo.jpg')

with col_2:
    st.title('Maksim Kudaev')
    st.info(description)

content_2 = """
Bellow you can find some of the apps I have built in Python.
"""
st.write(content_2)

col_3, col_4 = st.columns(2)

df = pandas.read_csv('data.csv', sep=';')

with col_3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col_4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
