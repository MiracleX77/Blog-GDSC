import json
from fastapi import HTTPException
from model.blog import RequestBlogData,BlogData, UpdateBlogData
from repository.auth import UserRepository
from repository.blog import BlogRepository


class BlogService:
    
    @staticmethod
    async def verifyData(data:RequestBlogData):
        if data.title == "":
            raise HTTPException(status_code=400,detail="Title Cannot Empty")
        if data.content == "":
            raise HTTPException(status_code=400,detail="Content Cannot Empty")
        user = await UserRepository.getOneById(data.user_id)
        if user == False:
            raise HTTPException(status_code=400,detail="User Not Found")
        blog = await BlogRepository.getOneByTitle(data.title,user["name"])
        if blog != False:
            raise HTTPException(status_code=400,detail="Title Already")
        pass
    
    @staticmethod
    async def create(data:RequestBlogData):
        user = await UserRepository.getOneById(data.user_id)
        data = BlogData(title=data.title,content=data.content,writer=user["name"])
        blog = await BlogRepository.create(data=data)
        if blog == False:
            raise HTTPException(status_code=400,detail="Create Failed")
        
    @staticmethod
    async def getAll():
        blogs = await BlogRepository.getAll()
        list_blogs = []
        for blog in blogs:
            blog = json.loads(json.dumps(blog,default=str))
            list_blogs.append(blog)
        return list_blogs
    
    @staticmethod
    async def getByNameWriter(user_id:str):
        user = await UserRepository.getOneById(id=user_id)
        blogs = await BlogRepository.getByNameWriter(name=user["name"])
        list_blogs = []
        for blog in blogs:
            blog = json.loads(json.dumps(blog,default=str))
            list_blogs.append(blog)
        return list_blogs
    
    @staticmethod
    async def getById(id:str):
        blog = await BlogRepository.getOneById(id=id)
        if blog == False:
            raise HTTPException(status_code=400,detail="Blog Not Found")
        blog = json.loads(json.dumps(blog,default=str))
        return blog
        
    @staticmethod
    async def verifyUpdateData(id:str,data:UpdateBlogData):
        if data.title == "":
            raise HTTPException(status_code=400,detail="Title Cannot Empty")
        if data.content == "":
            raise HTTPException(status_code=400,detail="Content Cannot Empty")
        blog = await BlogRepository.getOneById(id)
        if blog == False:
            raise HTTPException(status_code=400,detail="Blog Not Found")
        pass
    
    @staticmethod
    async def update(id:str,data:UpdateBlogData):
        blog = await BlogRepository.update(id=id,data=data)
        if blog == False:
            raise HTTPException(status_code=400,detail="Update Failed")
        
    @staticmethod
    async def delete(id:str):
        blog = await BlogRepository.delete(id=id)
        if blog == False:
            raise HTTPException(status_code=400,detail="Delete Failed")