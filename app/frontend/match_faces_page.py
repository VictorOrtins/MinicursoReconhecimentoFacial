import streamlit as st

from backend.face_recognition.face_recognition_engine import FaceRecognitionEngine
from backend.exceptions.multi_faces_exception import MultiFacesException
from backend.exceptions.no_faces_exception import NoFacesException


fr_engine = FaceRecognitionEngine()

st.title("Módulo de Reconhecimento Facial")

st.header("Compare se 2 imagens são da mesma pessoa")

col1, col2 = st.columns(2)

with col1:
    imagem1 = st.file_uploader("Imagem 1")
    if imagem1:
        st.image(imagem1)


with col2:
    imagem2 = st.file_uploader("Imagem 2")
    if imagem2:
        st.image(imagem2)


button_pressed = st.button("Comparar pessoas")
if button_pressed: ### Vai comparar as 2 pessoas
    if imagem1 and imagem2:
        try:
            same_person = fr_engine.match_faces(
                imagem1, 
                imagem2
            )
        except NoFacesException as e:
            st.error(e.msg)
            st.stop()
        except MultiFacesException as e:
            st.error(e.msg)
            st.stop()

        if same_person:
            st.success("As 2 imagens são da mesma pessoa")
        else:
            st.error("As 2 imagens não são da mesma pessoa")
    else:
        st.error("Selecione as 2 imagens")
