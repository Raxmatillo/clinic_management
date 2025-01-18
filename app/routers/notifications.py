from typing import List
from fastapi import APIRouter, Depends
from app.schemas.patients import ShowPatients
from app.database import get_db
from app.models.notifications import Notification
from sqlalchemy.orm import Session


router = APIRouter()


@router.get('/')
def all(db: Session=Depends(get_db)):
    return db.query(Notification).all()
