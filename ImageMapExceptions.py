class BaseImageMapException(Exception):
    def __init__(self, message):
        super().__init__(message)



class InvalidEdgeAmount(BaseImageMapException):
    pass
