from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class UserInput(BaseModel):
    name: str
    age: int


class User(BaseModel):
    id: int
    name: str
    age: int


@app.get("/", response_model=User)
async def hello(input: UserInput):
    return "Hello from happy-stock-api!"
