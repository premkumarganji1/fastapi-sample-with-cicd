# app/api/v1/routes.py
from fastapi import APIRouter
from app.models.schemas import Item
from app.services.sample_services import process_item

router = APIRouter()


@router.post("/items")
def create_item(item: Item):
    result = process_item(item)
    return {"message": "Item processed", "data": result}

@router.get("/items")
def get_item():
    return {"message": "Hey! It worked"}