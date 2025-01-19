from pydantic import BaseModel, Field
from datetime import date

from .courses import ShowCoursesSchemas
from .patients import ShowPatients

class ScheduleSchema(BaseModel):
    course_id: int = Field(
        ...,
        title="Course ID",
        description="Unique identifier for the course linked to the schedule.",
        example=202
    )
    course_day: int = Field(
        ...,
        title="Course Day",
        description="The specific day of the course for this schedule entry (e.g., 1 for the first day, 10 for the last day).",
        ge=1,
        example=5
    )
    attendance_date: date = Field(
        ...,
        title="Attendance Date",
        description="The date when the patient attended the course.",
        example="2025-01-18"
    )

    class Config:
        from_attributes = True
        json_schem_extra = {
            "example": {
                "course_id": 202,
                "course_day": 5,
                "attendance_date": "2025-01-18"
            }
        }

class ScheludeCoursesSchemas(BaseModel):
    course_id: int
    course_day: int
    attendance_date: date
    course: ShowCoursesSchemas
    class Config:
        from_attributes=True

class ScheludePatientsSchema(BaseModel):
    course_day: int
    attendance_date: date
    patient: ShowPatients  # 'PatientSchema' o'rnatilgan

    class Config:
        from_attributes = True


class UpdateScheduleSchema(BaseModel):
    course_day: int = Field(
        ...,
        title="Kurs kuni",
        description="The specific day of the course for this schedule entry (e.g., 1 for the first day, 10 for the last day).",
        ge=1,
        example=5
    )
    attendance_date: date = Field(
        ...,
        title="Davomat kuni",
        description="The date when the patient attended the course.",
        example="2025-01-18"
    )

    class Config:
        from_attributes: True