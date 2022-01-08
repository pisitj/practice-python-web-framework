from fastapi import APIRouter

router = APIRouter(prefix="/users")

@router.get("/")
def get_user_list():
    return {"message": "Get List of Users."}

@router.post("/")
def create_user():
    return {"message": "Create a User."}