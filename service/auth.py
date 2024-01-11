from fastapi import HTTPException
from repository.auth import UserRepository
from model.auth import RegisterData,LoginData,UserResponse,UserData

class RegisterService:
    
    @staticmethod
    async def verifyData(data:RegisterData):
        user = await UserRepository.getOneByUsername(data.username)
        if data.username == "":
            raise HTTPException(status_code=400,detail="Username Cannot Empty")
        if data.password == "":
            raise HTTPException(status_code=400,detail="Password Cannot Empty")
        if data.name == "":
            raise HTTPException(status_code=400,detail="Name Cannot Empty")
        if user != False:
            raise HTTPException(status_code=400,detail="Username Already")
        user = await UserRepository.getOneByName(data.name)
        if user != False:
            raise HTTPException(status_code=400,detail="Name Already")
            
        
    
    @staticmethod
    async def register(data:RegisterData):
        data = UserData(username=data.username,name=data.name,password=data.password)
        await UserRepository.create(data=data)
        
class LoginService:
    @staticmethod
    async def verifyData(data:LoginData):
        if data.username == "":
            raise HTTPException(status_code=400,detail="Username Cannot Empty")
        if data.password == "":
            raise HTTPException(status_code=400,detail="Password Cannot Empty")
        user = await UserRepository.getOneByUsername(data.username)
        if user == False:
            raise HTTPException(status_code=400,detail="User Not Found")
        if user["password"] != data.password:
            raise HTTPException(status_code=400,detail="Password Not Match")
        user = UserResponse(user_id=str(user["_id"]),name=user["name"])
        return user