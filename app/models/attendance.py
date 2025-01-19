from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Attendance(Base):
    __tablename__ = "attendance"

    attendance_id = Column(Integer, primary_key=True, index=True)
    schedule_id = Column(Integer, ForeignKey("schedules.schedule_id"), nullable=False)
    attendance_status = Column(String, nullable=False)
    note = Column(String, nullable=True)

    schedule = relationship("Schedule", back_populates="attendances")
