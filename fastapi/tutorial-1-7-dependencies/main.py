# https://fastapi.tiangolo.com/tutorial/dependencies/

from fastapi import FastAPI, Depends
from typing import Optional

app = FastAPI()

def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/")
def hello():
    return {"message": "Hello World."}

@app.get("/items")
def get_items(commons: dict = Depends(common_parameters)):
    return commons

@app.get("/users")
def get_users(commons: dict = Depends(common_parameters)):
    return commons
