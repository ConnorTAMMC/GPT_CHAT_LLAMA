import streamlit as st

with st.chat_message(name="user"):
    st.write("hello")
with st.chat_message(name="assistant"):
    st.write("hello yoyo ")
