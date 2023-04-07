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

col_3, empty_column, col_4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv('data.csv', sep=';')

with col_3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.write(f"[Source code]({row['url']})")
        st.image('images/' + row['image'])

with col_4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.write(f"[Source code]({row['url']})")
        st.image('images/' + row['image'])
