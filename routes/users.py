from fastapi import APIRouter

user_router = APIRouter(prefix="/users")

# http://localhost:8000/users/1234 형식의 요청을 처리하는 함수
@user_router.get("/{user_id}")
async def read_user(user_id: int) -> dict:
    return {"user_id": user_id}

# http://localhost:8000/users/
@user_router.post("/")
async def create_user(user: dict):
    return {"user": user}