from typing import TypeVar, Generic
from pydantic import BaseModel


T = TypeVar('T')
class ApiResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str = 'success'
    data: T = None
    code: int = 200