import os

import streamlit as st

page = st.navigation(
    [
        st.Page(os.path.join("frontend", "match_faces_page.py"), title="1:1", icon="🤝"),
        st.Page(os.path.join("frontend", "search_faces_page.py"), title="1:N", icon="🔍"),
    ]
)

page.run()
