from typing import Optional,TypeVar
from pydantic import BaseModel

T = TypeVar('T')

class ResponseData(BaseModel):
    message: str
    data: Optional[T] = None