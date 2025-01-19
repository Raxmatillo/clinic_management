from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.attendance import AttendanceSchema, ShowAttendanceSchemas
from app.database import get_db
from app.models.attendance import Attendance
from sqlalchemy.orm import Session


router = APIRouter()

@router.get('', response_model=List[ShowAttendanceSchemas])
async def all(db: Session = Depends(get_db)):
    return db.query(Attendance).all()

@router.post('/{schedule_id}', status_code=status.HTTP_201_CREATED)
async def create(schedule_id: int, request: AttendanceSchema, db: Session = Depends(get_db)):
    # Yangi Attendance yaratish
    new_attendance = Attendance(schedule_id=schedule_id, **request.dict())
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return new_attendance

@router.put('/{attendance_id}', status_code=status.HTTP_200_OK)
async def update_attendance(attendance_id: int, request: AttendanceSchema, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.attendance_id == attendance_id).first()
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance not found")
    
    for key, value in request.dict().items():
        setattr(attendance, key, value)
    db.commit()
    db.refresh(attendance)
    return attendance

@router.delete('/{attendance_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_attendance(attendance_id: int, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.attendance_id == attendance_id).first()
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance not found")
    
    db.delete(attendance)
    db.commit()
    return {"detail": "Attendance deleted successfully"}

