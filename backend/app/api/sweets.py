from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user, get_current_admin
from app.services.sweet_service import (
    create_sweet,
    get_all_sweets,
    purchase_sweet,
    restock_sweet
)

router = APIRouter(
    prefix="/api/sweets",
    tags=["sweets"]
)

@router.post("", status_code=201)
def add_sweet(
    payload: dict,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return create_sweet(db, payload)

@router.get("")
def list_sweets(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_all_sweets(db)

@router.post("/{sweet_id}/purchase")
def purchase(
    sweet_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return purchase_sweet(db, sweet_id)

@router.post("/{sweet_id}/restock")
def restock(
    sweet_id: int,
    payload: dict,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin)  # 🔒 ONLY ADMIN
):
    return restock_sweet(db, sweet_id, payload["amount"])
