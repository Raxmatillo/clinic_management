from pydantic import BaseModel, Field
from typing import Optional, List

from .schedules import ScheludePatientsSchema, ScheduleSchema


class AttendanceSchema(BaseModel):
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
        from_attributes = True
        json_schema_extra = {
            "example": {
                "attendance_status": "Present",
                "note": "Attended all sessions on time."
            }
        }

class ShowAttendanceSchemas(AttendanceSchema):
    # schedule: ScheduleSchema = []

    class Config:
        from_attributes=True