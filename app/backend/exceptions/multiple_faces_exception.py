class MultipleFacesException(Exception):
    """
    Exception raised when multiple faces are detected in an image.
    """

    def __init__(self, message="Multiple faces detected in the image."):
        self.message = message
        super().__init__(self.message)