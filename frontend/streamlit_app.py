import streamlit as st
import requests

st.title("Automated Book Scraper")

url = st.text_input("Enter chapter URL:")
chapter_id = st.text_input("Chapter ID", value="chapter1")

if st.button("Scrape"):
    r = requests.post("http://127.0.0.1:8000/scrape", json={"url": url, "chapter_id": chapter_id})
    st.write(r.json())
    st.image(f"http://127.0.0.1:8000/screenshot/{chapter_id}")
