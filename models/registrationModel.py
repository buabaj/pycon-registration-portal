from datetime import datetime
from pydantic import BaseModel, EmailStr


class attendee(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
