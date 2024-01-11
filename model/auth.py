from datetime import datetime
from pydantic import BaseModel

class UserData(BaseModel):
    username: str
    name: str
    password: str
    create_on: datetime = datetime.now()
    update_on: datetime = datetime.now()
    status :str = "Active"

class RegisterData(BaseModel):
    username: str
    password: str
    name: str
    
class LoginData(BaseModel):
    username: str
    password: str
    
class UserResponse(BaseModel):
    user_id: str
    name: str
