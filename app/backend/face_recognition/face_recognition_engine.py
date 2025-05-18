import cv2
import numpy as np

from deepface import DeepFace
from deepface.modules.verification import find_cosine_distance

from backend.exceptions.multiple_faces_exception import MultipleFacesException
from backend.exceptions.no_faces_exception import NoFacesException


class FaceRecognitionEngine:
    def __init__(self, fr_model: str = 'Facenet', fd_model: str = 'centerface'):
        self.face_recognition_model = fr_model
        self.face_detection_model = fd_model
        self.threshold = 0.4

    def match_faces(self, img1_bgr: cv2.Mat, img2_bgr: cv2.Mat) -> bool:
        """
        Match two faces using the specified face recognition model.
        :param img1: The first image containing a face.
        :param img2: The second image containing a face.
        :return: True if the faces match, False otherwise.
        """
        # Detect faces in both images
        try:
            detected_faces1 = self.__detect_faces(img1_bgr)
        except ValueError as e:
            raise NoFacesException("A imagem 1 deve conter exatamente uma face.") from e
        try:
            detected_faces2 = self.__detect_faces(img2_bgr)
        except ValueError as e:
            raise NoFacesException("A imagem 2 deve conter exatamente uma face.") from e
        
        if not self.__check_single_face_detected(detected_faces1):
            raise MultipleFacesException("A imagem 1 deve conter exatamente uma face.")
        
        if not self.__check_single_face_detected(detected_faces2):
            raise MultipleFacesException("A imagem 2 deve conter exatamente uma face.")
        
        face1 = np.array(detected_faces1[0]['face']*255)
        face2 = np.array(detected_faces2[0]['face']*255)

        template1 = np.array(self.__extract_template(face1)[0]['embedding'])
        template2 = np.array(self.__extract_template(face2)[0]['embedding'])


        cosine_distance = find_cosine_distance(template1, template2)
        if cosine_distance < self.threshold:
            return True

        return False
    
    def __detect_faces(self, img_bgr: cv2.Mat) -> list:
        """
        Detect faces in an image using the specified face detection model.
        :param img: The input image in which to detect faces.
        :return: A list of detected faces.
        """
        # Use DeepFace to detect faces
        detected_faces = DeepFace.extract_faces(img_bgr, detector_backend=self.face_detection_model)
        return detected_faces
    
    def __extract_template(self, img_bgr: cv2.Mat) -> list:
        """
        Extract face templates from an image using the specified face recognition model.
        :param img: The input image from which to extract face templates.
        :return: A list of extracted face templates.
        """
        # Use DeepFace to extract face templates
        face_templates = DeepFace.represent(img_bgr, model_name=self.face_recognition_model, detector_backend='skip', enforce_detection=False)
        return face_templates
    
    def __check_single_face_detected(self, detected_faces: list) -> bool:
        """
        Check if exactly one face is detected in the image.
        :param detected_faces: The list of detected faces.
        :return: True if exactly one face is detected, False otherwise.
        """
        return len(detected_faces) == 1
    

