import streamlit as st

st.set_page_config(page_title="Movie Recommender", layout="wide")

pg = st.navigation([
    st.Page("home.py",           title="🎬 Home"),
    st.Page("pages/analysis.py", title="📊 Analysis"),
])
pg.run()
