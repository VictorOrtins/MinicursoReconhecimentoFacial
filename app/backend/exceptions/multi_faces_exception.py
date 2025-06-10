"""
Exceção customizada para quando múltiplas faces são detectadas em uma imagem.
"""

class MultiFacesException(Exception):
    """
    Exceção lançada quando mais de uma face é detectada em uma imagem onde deveria haver apenas uma.
    
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