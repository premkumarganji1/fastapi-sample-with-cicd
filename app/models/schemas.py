# app/models/schemas.py
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float