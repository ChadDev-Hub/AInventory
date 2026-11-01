from fastapi import APIRouter
from core.logging import Logger
from datetime import datetime
router = APIRouter(prefix="/auth", tags=["auth"])
logger = Logger()
@router.post("/google")
async def google():
    print(datetime.now().astimezone())
    logger.loginfo("Logging in with Google")
    return {"message": "Logged in with Google"}

