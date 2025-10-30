from pydantic import BaseModel

class SandwichBase(BaseModel):
    name: str
    bread_type: str
    meat: str
    cheese: str | None = None
    sauce: str | None = None
    price: float

class SandwichCreate(SandwichBase):
    pass

class SandwichResponse(SandwichBase):
    id: int

    class Config:
        orm_mode = True
