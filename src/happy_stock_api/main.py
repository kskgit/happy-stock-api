# (1) 必要なライブラリをインポートする
import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL


# (2) User型を定義する
@strawberry.type
class User:
    name: str
    age: int


# (3) Query(データの読み込み)を行うクラスを定義する
@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Shota", age=22)


schema = strawberry.Schema(query=Query)
graphql_app: GraphQL[None, None] = GraphQL(schema)
app = FastAPI()
app.mount("/graphql", graphql_app)
