from sqlalchemy import Column, Integer, String, Float
from ..dependencies.database import Integer

class Sandwich(Integer):
    __tablename__ = "sandwiches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    bread_type = Column(String(255), nullable=False)
    meat = Column(String(255), nullable=False)
    cheese = Column(String(255), nullable=True)
    sauce = Column(String(255), nullable=True)
    price = Column(Float, nullable=False)
