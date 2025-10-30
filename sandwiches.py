from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies.database import get_sandwich
from ..models import models, schemas

router = APIRouter(prefix="/sandwiches", tags=["Sandwiches"])

@router.post("/", response_model=schemas.SandwichResponse)
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_sandwich)):
    new_sandwich = models.Sandwich(**sandwich.dict())
    db.add(new_sandwich)
    db.commit()
    db.refresh(new_sandwich)
    return new_sandwich

@router.get("/", response_model=list[schemas.SandwichResponse])
def get_sandwiches(db: Session = Depends(get_sandwich)):
    return db.query(models.Sandwich).all()

@router.get("/{id}", response_model=schemas.SandwichResponse)
def get_sandwich(id: int, db: Session = Depends(get_sandwich)):
    sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == id).first()
    if not sandwich:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwich

@router.put("/{id}", response_model=schemas.SandwichResponse)
def update_sandwich(id: int, sandwich: schemas.SandwichCreate, db: Session = Depends(get_sandwich)):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == id).first()
    if not db_sandwich:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    for key, value in sandwich.dict().items():
        setattr(db_sandwich, key, value)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

@router.delete("/{id}")
def delete_sandwich(id: int, db: Session = Depends(get_sandwich)):
    sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == id).first()
    if not sandwich:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    db.delete(sandwich)
    db.commit()
    return {"message": "Sandwich deleted"}
