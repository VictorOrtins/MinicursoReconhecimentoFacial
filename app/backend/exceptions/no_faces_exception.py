class NoFacesException(Exception):
    """Exception raised when no faces are detected in an image."""
    def __init__(self, message="No faces detected in the image."):
        self.message = message
        super().__init__(self.message)