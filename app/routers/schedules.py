from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas.schedules import ScheduleSchema, ScheludePatientsSchema, ScheludeCoursesSchemas, UpdateScheduleSchema
from app.database import get_db
from app.models.schedules import Schedule
from sqlalchemy.orm import Session
from app.models.patients import PatientCourses

router = APIRouter()


@router.get('/', response_model=List[ScheludeCoursesSchemas])
def all(db: Session = Depends(get_db)):
    all_patients = db.query(Schedule).all()
    return all_patients

# Ma'lum bir bemorning jadvalini olish
@router.get("/{patient_id}", response_model=List[ScheludePatientsSchema])
def get_schedules_by_patient_id(patient_id: int, db: Session = Depends(get_db)):
    schedules = db.query(Schedule).filter(Schedule.patient_id == patient_id).all()
    return schedules


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(patient_id: int, request: ScheduleSchema, db: Session=Depends(get_db)):
        # Tekshirish: bemor uchun ushbu kurs allaqachon mavjudmi?
    existing_schedule = db.query(Schedule).filter(
        Schedule.patient_id == patient_id,
        Schedule.course_id == request.course_id,
        Schedule.course_day == request.course_day
    ).first()

    if existing_schedule:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Schedule for this course and day already exists for the patient"
        )

    # Yangi jadvalni yaratish
    new_schedule = Schedule(**request.dict(), patient_id=patient_id)
    new_patient_course = PatientCourses(patient_id=patient_id, course_id=request.course_id)
    db.add(new_patient_course)
    db.add(new_schedule)
    db.commit()
    db.refresh(new_patient_course)
    db.refresh(new_schedule)
    return new_schedule


@router.put('/{schedule_id}', status_code=status.HTTP_200_OK)
def update_schedule(schedule_id: int, request: UpdateScheduleSchema, db: Session = Depends(get_db)):
    schedule = db.query(Schedule).filter(Schedule.schedule_id == schedule_id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    
    for key, value in request.dict().items():
        setattr(schedule, key, value)
    db.commit()
    db.refresh(schedule)
    return schedule

@router.delete('/{schedule_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_schedule(schedule_id: int, db: Session = Depends(get_db)):
    schedule = db.query(Schedule).filter(Schedule.schedule_id == schedule_id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    
    db.delete(schedule)
    db.commit()
    return {"detail": "Schedule deleted successfully"}
