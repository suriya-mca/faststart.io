from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/home")
def home():
    return "welcome!"