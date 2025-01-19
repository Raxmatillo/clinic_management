from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.patients import ShowPatients, PatientSchema, UpdatePatientSchema
from app.database import get_db
from app.models.patients import Patient
from sqlalchemy.orm import Session


router = APIRouter()

@router.get('/', response_model=List[ShowPatients])
def all(db: Session = Depends(get_db)):
    all_patients = db.query(Patient).all()
    return all_patients

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: PatientSchema, db: Session=Depends(get_db)):
    new_patient = Patient(full_name=request.full_name, birth_date=request.birth_date, phone_number=request.phone_number)
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

@router.put('/{patient_id}', status_code=status.HTTP_200_OK)
def update_patient(patient_id: int, request: UpdatePatientSchema, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    for key, value in request.dict().items():
        setattr(patient, key, value)
    db.commit()
    db.refresh(patient)
    return patient

@router.delete('/{patient_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    try:
        patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        
        db.delete(patient)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


