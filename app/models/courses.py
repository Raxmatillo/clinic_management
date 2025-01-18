from sqlalchemy import Column, Integer, String
from app.models.base import Base

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String, nullable=False)
    course_duration = Column(Integer, nullable=False)
    interval_duration = Column(Integer, nullable=False)
