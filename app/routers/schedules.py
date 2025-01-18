from typing import List
from fastapi import APIRouter, Depends, status
from app.schemas.schedules import ScheduleSchema
from app.database import get_db
from app.models.schedules import Schedule
from sqlalchemy.orm import Session


router = APIRouter()


@router.get('/', response_model=List[ScheduleSchema])
def all(db: Session = Depends(get_db)):
    all_patients = db.query(Schedule).all()
    return all_patients

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: ScheduleSchema, db: Session=Depends(get_db)):
    new_schedule = Schedule(course_day=request.course_day, attendance_date=request.attendance_date)
    db.add(new_schedule)
    db.commit()
    db.refresh(new_schedule)
    return new_schedule
