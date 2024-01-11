from bson import ObjectId
from config.database import mongo_connection

class BlogRepository:
    @staticmethod
    async def getOneByTitle(title:str,writer:str):
        blog = mongo_connection.set_collection("Blog").find_one({"title": title , "writer": writer,"status": "Active"})
        if blog:
            return blog
        else:
            return False
        
    @staticmethod
    async def getAll():
        blogs = mongo_connection.set_collection("Blog").find({"status": "Active"})
        if blogs:
            return blogs
        else:
            return False
        
    @staticmethod
    async def getOneById(id:str):
        blog = mongo_connection.set_collection("Blog").find_one({"_id": ObjectId(id) , "status": "Active"})
        if blog:
            return blog
        else:
            return False
        
    @staticmethod
    async def getByNameWriter(name:str):
        blogs = mongo_connection.set_collection("Blog").find({"writer": name , "status": "Active"})
        if blogs:
            return blogs
        else:
            return False
        
    @staticmethod
    async def create(data):
        blog = mongo_connection.set_collection("Blog").insert_one(data.model_dump())
        if blog:
            return blog
        else:
            return False
        
    @staticmethod
    async def update(id:str,data):
        blog = mongo_connection.set_collection("Blog").update_one({"_id": ObjectId(id)},{"$set": data.model_dump()})
        if blog:
            return blog
        else:
            return False
        
    @staticmethod
    async def delete(id:str):
        blog = mongo_connection.set_collection("Blog").update_one({"_id": ObjectId(id)},{"$set": {"status": "Inactive"}})
        if blog:
            return blog
        else:
            return False
    