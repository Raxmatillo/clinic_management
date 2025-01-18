from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.models.base import Base

class Schedule(Base):
    __tablename__ = "schedules"

    schedule_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.course_id"), nullable=False)
    course_day = Column(Integer, nullable=False)
    attendance_date = Column(Date, nullable=False)

    patient = relationship("Patient", back_populates="schedules")
    course = relationship("Course")

