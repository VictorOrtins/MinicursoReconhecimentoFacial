"""
Exceção customizada para quando nenhuma face é detectada em uma imagem.
"""

class NoFacesException(Exception):
    """
    Exceção lançada quando nenhuma face é detectada em uma imagem onde deveria haver pelo menos uma.
    
    Args:
        msg (str): Mensagem de erro descrevendo o problema
    """
    def __init__(self, msg):
        """
        Inicializa a exceção com uma mensagem descritiva.
        
        Args:
            msg (str): Mensagem de erro
        """
        self.msg = msg