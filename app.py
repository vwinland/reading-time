"""Run with: streamlit run app.py"""

import streamlit as st

from reading_time import estimate_minutes

st.set_page_config(page_title="Reading Time", page_icon="📖")
st.title("Reading Time")
st.write("Paste an article to estimate how long it takes to read.")
text = st.text_area("Your text", height=250, placeholder="Paste your writing here…")

if text.strip():
    minutes = estimate_minutes(text)
    st.metric("Estimated reading time", f"{minutes} {'minute' if minutes == 1 else 'minutes'}")
    st.caption(f"{len(text.split()):,} words · Assumes 200 words per minute, rounded up.")
else:
    st.info("Add some text to see your reading-time estimate.")
