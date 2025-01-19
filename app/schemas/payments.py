from pydantic import BaseModel, Field
from datetime import datetime

class PaymentSchema(BaseModel):
    payment_id: int = Field(
        ...,
        title="Payment ID",
        description="Unique identifier for the payment.",
        example=1
    )
    patient_id: int = Field(
        ...,
        title="Patient ID",
        description="Identifier of the patient who made the payment.",
        example=123
    )
    course_id: int = Field(
        ...,
        title="Course ID",
        description="Identifier of the course for which the payment was made.",
        example=10
    )
    amount_paid: float = Field(
        ...,
        title="Amount Paid",
        description="The amount paid by the patient for the course.",
        gt=0,
        example=150.0
    )
    payment_date: datetime = Field(
        default_factory=datetime.utcnow,
        title="Payment Date",
        description="The date and time when the payment was made.",
        example="2025-01-18T14:00:00"
    )
    payment_status: str = Field(
        default="partial",
        title="Payment Status",
        description="The current status of the payment (e.g., partial, full).",
        example="partial"
    )

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "payment_id": 1,
                "patient_id": 123,
                "course_id": 10,
                "amount_paid": 150.0,
                "payment_date": "2025-01-18T14:00:00",
                "payment_status": "partial"
            }
        }
