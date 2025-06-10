import numpy as np
import cv2

"""
Módulo com funções utilitárias para manipulação de imagens.
"""

def convert_img_to_array(imagem_upada):
    """
    Converte uma imagem enviada via Streamlit em um array numpy (BGR).
    
    Args:
        imagem_upada: Objeto FileUploader do Streamlit contendo a imagem
        
    Returns:
        numpy.ndarray: Array numpy representando a imagem no formato BGR
    """
    file_bytes = np.asarray(
        bytearray(imagem_upada.read()), 
        dtype=np.uint8
    )

    imagem_array = cv2.imdecode(
        file_bytes, 
        cv2.IMREAD_COLOR
    )

    return imagem_array