from sqlalchemy.orm import Session
from app.db.models import Sweet
from fastapi import HTTPException


def create_sweet(db: Session, data: dict):
    sweet = Sweet(**data)
    db.add(sweet)
    db.commit()
    db.refresh(sweet)
    return sweet

def get_all_sweets(db: Session):
    return db.query(Sweet).all()

def purchase_sweet(db: Session, sweet_id: int):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()

    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    if sweet.quantity <= 0:
        raise HTTPException(status_code=400, detail="Out of stock")

    sweet.quantity -= 1
    db.commit()
    db.refresh(sweet)
    return sweet

def restock_sweet(db: Session, sweet_id: int, amount: int):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()

    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    sweet.quantity += amount
    db.commit()
    db.refresh(sweet)
    return sweet
