from typing import List
from fastapi import APIRouter, Depends
from app.schemas.patients import ShowPatients
from app.database import get_db
from app.models.patients import Patient
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)