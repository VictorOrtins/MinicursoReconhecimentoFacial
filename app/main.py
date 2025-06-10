"""
Arquivo principal da aplicação Streamlit para reconhecimento facial.
Define a navegação entre as páginas de comparação 1:1 e busca 1:N.
"""

import streamlit as st

# Cria a navegação entre as páginas do frontend
page = st.navigation([
    st.Page("frontend/match_faces_page.py", title="1:1"), 
    st.Page("frontend/search_faces_page.py", title="1:N")
])

# Executa a página selecionada
page.run()