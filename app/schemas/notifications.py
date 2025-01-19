from pydantic import BaseModel, Field
from datetime import datetime

class NotificationSchema(BaseModel):
    notification_id: int = Field(
        ...,
        title="Notification ID",
        description="Unique identifier for the notification entry.",
        example=1
    )
    patient_id: int = Field(
        ...,
        title="Patient ID",
        description="Unique identifier linking this notification to a specific patient.",
        example=101
    )
    course_id: int = Field(
        ...,
        title="Course ID",
        description="Unique identifier linking this notification to a specific course.",
        example=201
    )
    notification_date: datetime = Field(
        ...,
        title="Notification Date",
        description="Date and time when the notification is scheduled or sent.",
        example="2025-01-18T10:30:00"
    )
    message: str = Field(
        ...,
        title="Message",
        description="The content of the notification message.",
        min_length=1,
        max_length=500,
        example="Your next session is scheduled for tomorrow at 10:00 AM."
    )

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "notification_id": 1,
                "patient_id": 101,
                "course_id": 201,
                "notification_date": "2025-01-18T10:30:00",
                "message": "Your next session is scheduled for tomorrow at 10:00 AM."
            }
        }
