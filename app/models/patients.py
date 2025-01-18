from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.models.base import Base
from datetime import datetime

class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    birth_date = Column(DateTime, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="active")

    schedules = relationship("Schedule", back_populates="patient")
    payments = relationship("Payment", back_populates="patient")
    notifications = relationship("Notification", back_populates="patient")
