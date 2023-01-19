from pydantic import BaseModel
from enum import Enum

class Category(str, Enum):
    Popular="Popular"
    Latest="Latest"
    



class Product(BaseModel):
    name: str
    description: str
    price: float | int
    category: Category