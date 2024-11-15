import streamlit as st
from ytmusicapi import YTMusic

ytm = YTMusic()

st.title("🎈 My new app")
st.write(ytm.search("hello", filter="songs"))
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
