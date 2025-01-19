from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.courses import CoursesSchemas, UpdateCourseSchema, ShowCoursesSchemas
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

@router.get('/{course_id}', response_model=ShowCoursesSchemas)
async def show(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.put('/{course_id}', status_code=status.HTTP_200_OK)
def update_course(course_id: int, request: UpdateCourseSchema, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    for key, value in request.dict().items():
        setattr(course, key, value)
    db.commit()
    db.refresh(course)
    return course

@router.delete('/{course_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    db.delete(course)
    db.commit()
    return {"detail": "Course deleted successfully"}