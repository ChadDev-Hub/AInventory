from fastapi import FastAPI
from modules.auth.routes.router import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from core.logging import Logger


Logger.setuplogging()

app = FastAPI()
app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}







