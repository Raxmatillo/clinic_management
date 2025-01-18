from pydantic import BaseModel, Field
from datetime import date

class ScheduleSchema(BaseModel):
    schedule_id: int = Field(
        ...,
        title="Schedule ID",
        description="Unique identifier for the schedule entry.",
        example=1
    )
    patient_id: int = Field(
        ...,
        title="Patient ID",
        description="Unique identifier for the patient linked to the schedule.",
        example=101
    )
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
        orm_mode = True
        schema_extra = {
            "example": {
                "schedule_id": 1,
                "patient_id": 101,
                "course_id": 202,
                "course_day": 5,
                "attendance_date": "2025-01-18"
            }
        }
