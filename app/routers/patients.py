from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.patients import ShowPatients, PatientSchema
from app.database import get_db
from app.models import patients
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)

@router.get('/', response_model=List[ShowPatients])
def all(db: Session = Depends(get_db)):
    all_patients = db.query(patients.Patient).all()
    return all_patients

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: PatientSchema, db: Session=Depends(get_db)):
    new_patient = patients.Patient(full_name=request.full_name, birth_date=request.birth_date, phone_number=request.phone_number)
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient
