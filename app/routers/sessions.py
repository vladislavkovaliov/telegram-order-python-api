from fastapi import APIRouter, Response, Request
from app.services.sessions import create_session

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.get("/start_session")
async def start_session(response: Response, request: Request):
    return await create_session(request)


@router.get("/check_session")
async def check_session(response: Response, request: Request):
    session_id = request.cookies.get("session_id")

    return {"session_id": session_id}