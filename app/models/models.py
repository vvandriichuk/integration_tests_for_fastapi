from pydantic import BaseModel
from typing import List, Optional


class Item(BaseModel):

    title: str
    description: Optional[str]
    quantity: int
    price: float


class Order(BaseModel):

    id: str
    status: str
    items: List[Item]
    total_price: float
