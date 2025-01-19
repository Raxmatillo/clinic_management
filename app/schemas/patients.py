from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr
from datetime import date, datetime

from .courses import CoursesSchemas

class PatientSchema(BaseModel):
    full_name: str = Field(
        ...,
        title="Full Name",
        description="The full name of the patient.",
        min_length=1,
        max_length=100,
        example="John Doe"
    )
    birth_date: date = Field(
        ...,
        title="Birth Date",
        description="The date of birth of the patient.",
        example="1985-07-15"
    )
    phone_number: str = Field(
        ...,
        title="Phone Number",
        description="The contact phone number of the patient.",
        min_length=10,
        max_length=15,
        example="+1234567890"
    )
    status: str = Field(
        default="active",
        title="Status",
        description="The current status of the patient (e.g., active, inactive).",
        example="active"
    )

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "patient_id": 1,
                "full_name": "John Doe",
                "birth_date": "1985-07-15",
                "phone_number": "+1234567890",
                "created_at": "2025-01-18T14:00:00",
                "status": "active"
            }
        }


class ShowPatients(BaseModel):
    full_name: str
    birth_date: datetime
    phone_number: str
    courses: List[CoursesSchemas] = []

    class Config():
        from_attribs=True


class UpdatePatientSchema(BaseModel):
    full_name: Optional[str] = Field(None, example="Rakhatullo Shermatov")
    birth_date: Optional[date] = Field(None, example="1985-07-18")
    phone_number: Optional[str] = Field(None, example="+998901234567")
    status: Optional[str] = Field(None, example="active")

    class Config:
        from_attributes = True