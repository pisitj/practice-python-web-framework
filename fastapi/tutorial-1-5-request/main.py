from fastapi import FastAPI, Query, Path, Body
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    firstname: Optional[str] = None
    lastname: Optional[str] = None

@app.get("/")
def hello():
    return {"message": "Hello World."}

# query parameter
# https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
@app.get("/users")
def query_user(id: Optional[str] = Query(...)):
    return {"id": id}

# path parameter
# https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
@app.get("/users/{id}")
def get_user_by_id(id: str = Path(...)):
    return {"id": id}

# request body
# https://fastapi.tiangolo.com/tutorial/body-multiple-params/
@app.post("/users")
def create_user(data: User = Body(...)):
    return data
