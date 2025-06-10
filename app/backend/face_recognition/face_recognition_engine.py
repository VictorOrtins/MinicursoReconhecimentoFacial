"""
Módulo principal de reconhecimento facial.
Utiliza a biblioteca DeepFace para extrair características faciais e realizar comparações.
"""

from deepface import DeepFace
from deepface.modules.verification import find_cosine_distance

from backend.utils.utils import convert_img_to_array
from backend.exceptions.no_faces_exception import NoFacesException
from backend.exceptions.multi_faces_exception import MultiFacesException

class FaceRecognitionEngine:
    """
    Engine de reconhecimento facial que gerencia extração de características e comparação de faces.
    
    Attributes:
        fr_model (str): Modelo usado para reconhecimento facial (Facenet por padrão)
        fd_model (str): Modelo usado para detecção facial (centerface por padrão)
        threshold (float): Limiar de similaridade para considerar faces como matching
    """
    def __init__(self):
        """
        Inicializa o engine de reconhecimento facial com modelos padrão.
        """
        self.fr_model = 'Facenet' #Dlib, Facenet-512, GhostFaceNet
        self.fd_model = 'centerface' #dlib, mtcnn, retinaface
        self.threshold = 0.4

    def match_faces(self, img1, img2):
        """
        Compara duas imagens e verifica se são da mesma pessoa.
        Args:
            img1: Imagem 1 (arquivo upado)
            img2: Imagem 2 (arquivo upado)
        Returns:
            bool: True se forem da mesma pessoa, False caso contrário
        """

        img1 = convert_img_to_array(img1)
        img2 = convert_img_to_array(img2)

        template1 = self.__extract_template(img1, 1)
        self.__check_single_face_detected(template1, 1)
        template1 = template1[0]['embedding']

        template2 = self.__extract_template(img2, 2)
        self.__check_single_face_detected(template2, 2)
        template2 = template2[0]['embedding']

        same_person = self.__compare_templates(template1, 
                                               template2)
        
        return same_person
    
    def __extract_template(self, img, num_img):
        """
        Extrai o template (embedding) facial de uma imagem.
        Args:
            img: Array numpy da imagem
            num_img: Índice da imagem (para mensagens de erro)
        Returns:
            list: Lista de embeddings extraídos
        Raises:
            NoFacesException: Se nenhuma face for detectada
        """
        try:
            template = DeepFace.represent(
                img, 
                model_name=self.fr_model,
                detector_backend=self.fd_model
            )
        except ValueError: #Detectou nenhuma face
            raise NoFacesException(f"""
            A imagem {num_img} não possui nenhuma face""")

        return template #LISTA

    def __check_single_face_detected(self, templates, num_img):
        """
        Verifica se apenas uma face foi detectada na imagem.
        Args:
            templates: Lista de embeddings extraídos
            num_img: Índice da imagem (para mensagens de erro)
        Raises:
            MultiFacesException: Se mais de uma face for detectada
        """
        qtd_templates = len(templates)

        if qtd_templates > 1:
            raise MultiFacesException(f"""
            A imagem {num_img} possui mais de uma face""")

    def __compare_templates(self, template1, template2):
        """
        Compara dois embeddings faciais usando distância do cosseno.
        Args:
            template1: Embedding da imagem 1
            template2: Embedding da imagem 2
        Returns:
            bool: True se forem da mesma pessoa, False caso contrário
        """
        distance = find_cosine_distance(template1, template2)

        if distance > self.threshold: #Muito distantes
            return False #Templates de pessoas diferentes
        else: # Templates próximos
            return True #Templates da mesma pessoa