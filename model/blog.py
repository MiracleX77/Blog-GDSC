from datetime import datetime 
from pydantic import BaseModel

class BlogData(BaseModel):
    title: str
    content: str
    writer: str
    create_on: datetime = datetime.now()
    update_on: datetime = datetime.now()
    status: str = "Active"
    
class RequestBlogData(BaseModel):
    title: str
    content: str
    user_id: str
    
class UpdateBlogData(BaseModel):
    title: str
    content: str
