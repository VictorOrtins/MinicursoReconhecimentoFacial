import streamlit as st

from backend.face_recognition.face_recognition_engine import FaceRecognitionEngine
from backend.exceptions.multiple_faces_exception import MultipleFacesException
from backend.utils.image_utils import convert_img_to_array

engine = FaceRecognitionEngine()

st.title("Módulo de Comparação de Imagens")

st.header("Comparar duas imagens para verificar se são da mesma pessoa")

# Permite upload de imagem
image1 = st.file_uploader("Faça upload da primeira imagem", type=["jpg", "jpeg", "png"])
image2 = st.file_uploader("Faça upload da segunda imagem", type=["jpg", "jpeg", "png"])


col1, col2 = st.columns(2)
with col1:
    if image1:
        st.image(image1, caption="Imagem 1", use_container_width=True)
with col2:
    if image2:
        st.image(image2, caption="Imagem 2", use_container_width=True)

if st.button("Comparar Imagens"):
    if image1 is None or image2 is None:
        st.error("Por favor, faça upload de ambas as imagens.")
    else:
        np_image_1 = convert_img_to_array(image1)
        np_image_2 = convert_img_to_array(image2)

        try:
            result = engine.match_faces(np_image_1, np_image_2)
        except MultipleFacesException as e:
            st.error(f"Erro: {e}")
            st.stop()

        if result:
            st.success("As imagens são da mesma pessoa!")
        else:
            st.error("As imagens não são da mesma pessoa.")
