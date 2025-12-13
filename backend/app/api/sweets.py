from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.services.sweet_service import create_sweet, get_all_sweets

router = APIRouter(
    prefix="/api/sweets",
    tags=["sweets"],
    dependencies=[Depends(get_current_user)]
)

@router.post("", status_code=201)
def add_sweet(payload: dict, db: Session = Depends(get_db)):
    return create_sweet(db, payload)

@router.get("")
def list_sweets(db: Session = Depends(get_db)):
    return get_all_sweets(db)
