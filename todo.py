from fastapi import APIRouter

todo_router = APIRouter(prefix="/todos")

# 할 일 정보를 저장할 리스트 => 이후에 DB 연동으로 변경
# 자바의 배열 같은 경우는 선언한 타입만 저장할 수 있고 크기가 고정적임
# 파이썬과 자바 스크립트의 리스트는 크기가 가변적이고 타입도 가변적임

# 테이블 형태의 구조에서 세로로 증가하는 값은 순번 ( 배열, 리스트 ) 0, 1, 2
# 테이블 형태의 구조에서 가로로 증가하는 값은 키,밸류 ( 딕셔너리, 리스트 ) - {"이름": 홍길동}
todo_list = []

#-----------------------------
# 할 일 데이터를 저장할 모델 정의
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str
#-----------------------------

# 할 일 추가
# POST http://localhost:8000/todos
@todo_router.post("")
async def add_todo(todo: Todo) -> dict:
    # todo_list 리스트에 todo 변수의 내용을 추가
    todo_list.append(todo)
    return {"message": "할 일을 추가했습니다."}

# 할 일 목록 조회
# GET http://localhost:8000/todos
@todo_router.get("")
async def retrives_todos() -> dict:
    return {"todos": todo_list}

# 할 일 상세 조회
# GET http://localhost:8000/todos/1
@todo_router.get("/{todo_id}")
async def retrive_todo(todo_id: int) -> dict:
    # todo_list 변수에는 아래와 같은 형식의 값이 지정
    # [ { id: 1, item: "파이썬 공부"}, {id: 2, item: "FastAPI"}]
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "일치하는 할 일이 없습니다."}