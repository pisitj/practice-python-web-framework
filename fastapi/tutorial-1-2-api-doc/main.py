# https://fastapi.tiangolo.com/

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

tags_metadata = [
    {
        "name": "items",
        "description": "Manage items",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/"
        }
    }
]

# Default with Interactive API docs
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc
# app = FastAPI()

# Metadata
# https://fastapi.tiangolo.com/tutorial/metadata/
app = FastAPI(
    title="Item API",
    description="Auto-generated API Doc by FastAPI",
    version="1.0.0",
    openapi_tags=tags_metadata
)

# Disable API docs
# https://fastapi.tiangolo.com/advanced/extending-openapi/?h=disable#disable-the-automatic-docs
# app = FastAPI(docs_url=None, redoc_url=None)

class Item(BaseModel):
    name: str
    price: float
    detail: Optional[str] = None

@app.get("/")
def hello():
    return {"message": "Hello World."}

@app.get("/items/{item_id}", tags=["items"], description="Get an item by ID")
def get_item_by_id(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}", tags=["items"], deprecated=True)
def update_item_by_id(item_id: int, item: Item):
    """
    Update an item by ID.
    """
    return {"id": item_id, "name": item.name, "price": item.price, "detail": item.detail}
