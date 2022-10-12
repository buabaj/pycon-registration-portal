from fastapi import APIRouter
from data.registrationDB import data
from models.registrationModel import attendee
from datetime import datetime

router = APIRouter()


@router.post("/register")
def register(attendee: attendee):
    registration_time = datetime.now()
    attendee = attendee.dict()
    attendee['registration_time'] = registration_time
    data.append(attendee)
    return {"message": "registration successful", "data": data[-1]}
