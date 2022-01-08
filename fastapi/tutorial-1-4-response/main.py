# https://fastapi.tiangolo.com/advanced/custom-response/

# Response
# JSONResponse (default)
# PlainTextResponse
# HTMLResponse
# RedirectResponse
# StreamingResponse
# FileResponse

from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse, HTMLResponse, RedirectResponse

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World."}  # default = JSONResponse

@app.get("/json")
def hello_json():
    return JSONResponse({"messsage": "Hello JSON."})

@app.get("/html")
def hello_html():
    return HTMLResponse("<h1>Hello HTML.</h1>")

@app.get("/redirect")
def hello_redirect():
    return RedirectResponse("/")

@app.get("/custom-response")
def hello_custom_response():
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    return Response(content=data, media_type="application/xml")