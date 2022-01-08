# https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-the-apirouters-for-users-and-items

from fastapi import FastAPI

from routers import items, users

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
def hello():
    return {"message": "Hello World."}