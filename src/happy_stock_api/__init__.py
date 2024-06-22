from fastapi import FastAPI

app = FastAPI()


# class UserInput(BaseModel):
#     name: str
#     age: int


# class User(BaseModel):
#     id: int
#     name: str
#     age: int


# TODO returun 型不一致だが警告が出ていない
@app.get("/")
async def hello():
    return "Hello from happy-stock-api!"
