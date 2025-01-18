from pydantic import BaseModel, Field
from typing import Optional

class AttendanceSchema(BaseModel):
    attendance_id: int = Field(
        ...,
        title="Attendance ID",
        description="Unique identifier for the attendance entry.",
        example=1
    )
    schedule_id: int = Field(
        ...,
        title="Schedule ID",
        description="Unique identifier linking this attendance entry to a schedule.",
        example=101
    )
    attendance_status: str = Field(
        ...,
        title="Attendance Status",
        description="The attendance status for the schedule entry (e.g., 'Present', 'Absent', 'Excused').",
        min_length=1,
        max_length=50,
        example="Present"
    )
    note: Optional[str] = Field(
        None,
        title="Note",
        description="Optional note for this attendance entry, such as additional details or reasons for absence.",
        max_length=255,
        example="Late arrival due to traffic."
    )

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "attendance_id": 1,
                "schedule_id": 101,
                "attendance_status": "Present",
                "note": "Attended all sessions on time."
            }
        }
