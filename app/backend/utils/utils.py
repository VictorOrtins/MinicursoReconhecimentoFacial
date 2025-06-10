import numpy as np
import cv2

def convert_img_to_array(imagem_upada):
    file_bytes = np.asarray(
        bytearray(imagem_upada.read()), 
        dtype=np.uint8
    )

    imagem_array = cv2.imdecode(
        file_bytes, 
        cv2.IMREAD_COLOR
    )

    return imagem_array