import uuid

from fastapi import Request, Response
from fastapi.responses import JSONResponse


async def create_uuid_and_save_redis(request) -> str:
    session_id = str(uuid.uuid4())
    redis = request.app.state.redis

    await redis.set(session_id, "active", ex=60 * 30)  # 30 min

    return session_id


async def create_session(request: Request):
    session_id = await create_uuid_and_save_redis(request)

    response = JSONResponse(content={"message": "Session started"})
    response.set_cookie(
        key="session_id",
        value=str(session_id),
        httponly=True,  # secure cookie
        max_age=60 * 30,   # 30min
        samesite="lax",
        secure=False    # Set to True in production (for HTTPS)
    )

    return response


# async def ensure_session(request: Request, response: Response):
#     session_id = request.cookies.get("session_id")
#     redis = request.app.state.redis
#
#     if not session_id or not await redis.exists(session_id):
#         session_id = str(uuid.uuid4())
#
#         await redis.set(session_id, "active", ex=3600)
#
#         response.set_cookie(
#             key="session_id",
#             value=session_id,
#             httponly=True,
#             max_age=3600,
#             samesite="lax",
#             secure=False  # set True if using HTTPS
#         )
#
#     request.state.session_id = session_id