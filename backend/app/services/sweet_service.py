from sqlalchemy.orm import Session
from app.db.models import Sweet

def create_sweet(db: Session, data: dict):
    sweet = Sweet(**data)
    db.add(sweet)
    db.commit()
    db.refresh(sweet)
    return sweet

def get_all_sweets(db: Session):
    return db.query(Sweet).all()
