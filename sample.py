from fastapi import FastAPI
from routes import users, items

app = FastAPI()
app.include_router(users.user_router)
app.include_router(items.item_router)

@app.get("/")
async def read_root():
    return {"message": "Hello World!"}

# @app.post("/items/")
# async def create_item(item: dict):
#    return {"received": item}

# @app.get("/items/{item_id}") # 경로 items 밑에 어떤 값을 받고 싶다.
# async def read_item(item_id: int):
#    return {"item_id": item_id}