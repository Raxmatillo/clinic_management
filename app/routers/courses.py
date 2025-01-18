from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.courses import CoursesSchemas
from app.database import get_db
from app.models.courses import Course
from sqlalchemy.orm import Session


router = APIRouter()

@router.get('/')
def all(db: Session=Depends(get_db)):
    return db.query(Course).all()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: CoursesSchemas, db: Session=Depends(get_db)):
    new_course = Course(course_name=request.course_name, course_duration=request.course_duration, interval_duration=request.interval_duration)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course