from fastapi import APIRouter

router = APIRouter(prefix="/items")

@router.get("/")
def get_item_list():
    return {"message": "Get List of Items."}

@router.post("/")
def create_item():
    return {"message": "Create a Item."}