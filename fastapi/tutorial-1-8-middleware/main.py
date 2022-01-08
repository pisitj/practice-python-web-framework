# https://fastapi.tiangolo.com/tutorial/middleware/

from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # request
    start_time = time.time()

    # next
    response = await call_next(request)

    # response
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get("/")
def hello():
    return {"message": "Hello World."}