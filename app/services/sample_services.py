# app/services/sample_service.py
from app.models.schemas import Item

def process_item(item: Item):
    return {
        "name": item.name.upper(),
        "price_with_tax": item.price * 1.18
    }