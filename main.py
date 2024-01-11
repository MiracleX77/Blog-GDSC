from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from config.database import mongo_connection


def intialized_app():
    
    @asynccontextmanager
    async def lifespan(app:FastAPI):
            mongo_connection.set_database('blog')
            yield
            mongo_connection.client.close()
    
    app = FastAPI(lifespan=lifespan)
    
    @app.get('/')
    async def index():
        return {'message': 'Hello World'}
    
    from controller.auth import router as auth_router
    app.include_router(auth_router)
    from controller.blog import router as blog_router
    app.include_router(blog_router)
    
    return app

app = intialized_app() 
if __name__ == "__main__":
    #uvicorn.run(app, host="127.0.0.1", port=8000)
    # deploy
    uvicorn.run(app, host="0.0.0.0", port=8000)