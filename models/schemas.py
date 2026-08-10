from pydantic import BaseModel

class ShoppingRequest(BaseModel):
    product: str
    budget: int
    preferences: list[str]