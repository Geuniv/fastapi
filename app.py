from fastapi import FastAPI

# FastAPI ( 웹 ) 인스턴스 생성
app = FastAPI()


# 라우트 정의
@app.get("/") # 얘가 딕셔너리를 사용자에게 JSON으로 바꿔서 보여준답니다.
async def welcome() -> dict: # async는 비동기로 실행한다고 선언해주는 함수 ( -> dict 는 데이터 형식 지정 지금은 Dictionary로 선언 )
    return {"message" : "Hello, world !"}

# todo.py 파일에 정의한 라우트 설정을 통합
from todo import todo_router

app.include_router(todo_router)