from fastapi import APIRouter,HTTPException
from model.response import ResponseData
from model.auth import RegisterData,LoginData
from service.auth import RegisterService,LoginService
router = APIRouter(
    prefix='/auth',
    tags=['auth'],
    responses = {404: {'description': 'Not found'}}
)

@router.post('/register',response_model=ResponseData,response_model_exclude_none=True)
async def register(data : RegisterData):
    await RegisterService.verifyData(data=data)
    await RegisterService.register(data=data)
    return ResponseData(message="Register Success")
    
@router.post('/login',response_model=ResponseData,response_model_exclude_none=True)
async def login(data: LoginData):
    res = await LoginService.verifyData(data=data)
    return ResponseData(message="Login Success",data=res)