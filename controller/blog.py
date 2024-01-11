from fastapi import APIRouter,HTTPException

from model.response import ResponseData
from model.blog import RequestBlogData, UpdateBlogData
from service.blog import BlogService

router = APIRouter(
    prefix='/blog',
    tags=['blog'],
    responses = {404: {'description': 'Not found'}}
)

@router.post('/create',response_model=ResponseData,response_model_exclude_none=True)
async def create(data:RequestBlogData):
    await BlogService.verifyData(data=data)
    await BlogService.create(data=data)
    return ResponseData(message="Create Success")

@router.get('/getAll',response_model=ResponseData,response_model_exclude_none=True)
async def getAll():
    res = await BlogService.getAll()
    return ResponseData(message="Get All Success",data=res)

@router.get('/getByUserId/{user_id}',response_model=ResponseData,response_model_exclude_none=True)
async def getByUserId(user_id:str):
    res = await BlogService.getByNameWriter(user_id=user_id)
    return ResponseData(message="Get By User Id Success",data=res)

@router.get('/getById/{id}',response_model=ResponseData,response_model_exclude_none=True)
async def getById(id:str):
    res = await BlogService.getById(id=id)
    return ResponseData(message="Get By Id Success",data=res)

@router.put('/update/{id}',response_model=ResponseData,response_model_exclude_none=True)
async def update(id:str,data:UpdateBlogData):
    await BlogService.verifyUpdateData(id=id,data=data)
    await BlogService.update(id=id,data=data)
    return ResponseData(message="Update Success")

@router.delete('/delete/{id}',response_model=ResponseData,response_model_exclude_none=True)
async def delete(id:str):
    await BlogService.delete(id=id)
    return ResponseData(message="Delete Success")