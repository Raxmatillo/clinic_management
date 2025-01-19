from sqlalchemy import Column, Integer, String, Date, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
from datetime import datetime

class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    phone_number = Column(String, nullable=False)
    # address = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="active")

    courses = relationship("Course", secondary="patient_courses", back_populates="patients")


    schedules = relationship("Schedule", back_populates="patient", cascade="all, delete-orphan")
    payments = relationship("Payment", back_populates="patient", cascade="all, delete")
    notifications = relationship("Notification", back_populates="patient", cascade="all, delete")

class PatientCourses(Base):
    __tablename__ = "patient_courses"

    patient_id = Column(Integer, ForeignKey("patients.patient_id", ondelete='CASCADE'), primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.course_id", ondelete='CASCADE'), primary_key=True)

