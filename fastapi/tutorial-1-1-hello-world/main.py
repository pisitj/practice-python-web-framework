# https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World."}

# start server (development)
# uvicorn main:app --port=3000 --reload

# main      the file main.py (the Python "module").
# app       the object created inside of main.py with the line app = FastAPI().

# --port    Bind socket to this port.  [default: 8000]
# --reload  make the server restart after code changes.
