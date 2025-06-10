import streamlit as st

page = st.navigation([
    st.Page("frontend/match_faces_page.py", title="1:1"), 
    st.Page("frontend/search_faces_page.py", title="1:N")
])

page.run()