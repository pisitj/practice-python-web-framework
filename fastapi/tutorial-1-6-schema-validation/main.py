# https://fastapi.tiangolo.com/tutorial/response-model/

from fastapi import FastAPI, Body
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    username: str
    password: str
    email: str
    firstname: Optional[str] = None
    lastname: Optional[str] = None

class UserOutput(BaseModel):
    username: str
    # password: str # password should not be returned.
    email: str
    firstname: Optional[str] = None
    lastname: Optional[str] = None

@app.get("/")
def hello():
    return {"message": "Hello World."}

@app.post("/users", response_model=UserOutput)
def create_user(user: UserInput = Body(...)):
    return user

# UserInput
# {
#     "username": "xxx",
#     "password": "yyy",
#     "email": "aaa.bbb@gmail.com",
#     "firstname": "aaa",
#     "lastname": "bbb"
# }

# UserOutput
# {
#     "username": "xxx",
#     "email": "aaa.bbb@gmail.com",
#     "firstname": "aaa",
#     "lastname": "bbb"
# }
