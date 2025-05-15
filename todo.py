from fastapi import APIRouter, Path, Query
from model import Todo


todo_router = APIRouter(prefix="/todos")

# 할 일 정보를 저장할 리스트 => 이후에 DB 연동으로 변경
# 자바의 배열 같은 경우는 선언한 타입만 저장할 수 있고 크기가 고정적임
# 파이썬과 자바 스크립트의 리스트는 크기가 가변적이고 타입도 가변적임

# 테이블 형태의 구조에서 세로로 증가하는 값은 순번 ( 배열, 리스트 ) 0, 1, 2
# 테이블 형태의 구조에서 가로로 증가하는 값은 키,밸류 ( 딕셔너리, 리스트 ) - {"이름": 홍길동}
todo_list = []

# 해당 부분을 model.py로 분리리
#-----------------------------
# 할 일 데이터를 저장할 모델 정의
# from pydantic import BaseModel

# class Todo(BaseModel):
#     id: int
#     item: str
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

# 할 일 검색
# 할 일 검색 기능에 item 항목의 값을 필수 입력으로, 최소 2자리, 최대 10자리로 설정
# http://localhost:8000/todos/search?item=검색어
@todo_router.get("/search")
async def search_todos(item: str = Query(..., min_length=2, max_length=10, title="할 일 목록 검색어")) -> dict:
    result = []
    for todo in todo_list:
        if item in todo.item:
            result.append(todo)
    return {"todos": result}

# 할 일 상세 조회
# GET http://localhost:8000/todos/1
@todo_router.get("/{todo_id}")
async def retrive_todo(todo_id: int = Path(..., title="조회할 할 일의 ID", ge=1)) -> dict:
    # todo_list 변수에는 아래와 같은 형식의 값이 지정
    # [ { id: 1, item: "파이썬 공부"}, {id: 2, item: "FastAPI"}]
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
        
    return {"message": "일치하는 할 일이 없습니다."}

# 할 일 수정
@todo_router.put("/{todo_id}")
async def update_todo(todo_id: int = Path(..., title="수정할 할 일의 ID", ge=1), new_todo: Todo = None) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = new_todo.item
            return {"message": "할 일을 수정했습니다."}
    return {"message": "일치하는 할 일이 없습니다."}

# 할 일 삭제
@todo_router.delete("/{todo_id}")
async def delete_todo(todo_id: int = Path(..., title="삭제할 할 일의 ID", ge=1)) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo_list.remove(todo)
            return {"message": "할 일을 삭제했습니다."}
    return {"message": "일치하는 할 일이 없습니다."}