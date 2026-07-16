from fastapi import status
from cores.exception_handler import AppException


class UnauthorizedException(AppException):
    """未授權的例外"""
    def __init__(
        self, 
        message: str = "未授權", 
        status_code: int = status.HTTP_401_UNAUTHORIZED
    ):
        super().__init__(message, status_code)