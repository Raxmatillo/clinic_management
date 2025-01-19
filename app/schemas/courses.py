from typing import Optional, List
from pydantic import BaseModel, Field



class CoursesSchemas(BaseModel):
    course_name: str = Field(
        ...,
        title="Course Name",
        description="The name of the course being offered (e.g., 'Physiotherapy Basics').",
        min_length=3,
        max_length=100,
        example="Advanced Physiotherapy"
    )
    course_duration: int = Field(
        ...,
        title="Course Duration (Days)",
        description="The total number of days for this course. For example, a 10-day course would be '10'.",
        ge=1,
        le=365,
        example=10
    )
    interval_duration: int = Field(
        ...,
        title="Interval Duration (Days)",
        description="The interval between courses in days. For example, a 1-month interval would be '30'.",
        ge=1,
        le=90,
        example=30
    )

    class Config:
        json_schema_extra = {
            "example": {
                "course_name": "Advanced Physiotherapy",
                "course_duration": 10,
                "interval_duration": 30
            }
        }

class ShowCoursesSchemas(CoursesSchemas):
    class Config:
        from_attributes=True


class UpdateCourseSchema(BaseModel):
    course_name: Optional[str] = Field(None, example="1-kurs", title="Kurs nomi")
    course_duration: Optional[int] = Field(..., ge=1, le=10, title="Kurs davomi (kun)")
    course_interval: Optional[int] = Field(..., ge=1, le=30, title="Kurslar oralig'i (kun)")

    class Config:
        from_attributes=True