from bson import ObjectId
from config.database import mongo_connection

class UserRepository:
    
    @staticmethod
    async def getOneById(id:str):
        user = mongo_connection.set_collection("User").find_one({"_id": ObjectId(id) , "status": "Active"})
        if user:
            return user
        else:
            return False
    @staticmethod
    async def getOneByUsername(username:str):
        user = mongo_connection.set_collection("User").find_one({"username": username , "status": "Active"})
        if user:
            return user
        else:
            return False
        
    @staticmethod
    async def getOneByName(name:str):
        user = mongo_connection.set_collection("User").find_one({"name": name , "status": "Active" })
        if user:
            return user
        else:
            return False
        
    @staticmethod
    async def create(data):
        user = mongo_connection.set_collection("User").insert_one(data.model_dump())
        if user:
            return user
        else:
            return False