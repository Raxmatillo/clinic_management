from typing import List
from pydantic import BaseModel
from datetime import date


class NewPatients(BaseModel):
    full_name: str
    birth_data: date
    phone_number: str

class ShowPatients(BaseModel):
    full_name: str
    birth_data: date
    phone_number: str

    class Config():
        from_attributes=True