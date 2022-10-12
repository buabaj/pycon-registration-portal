from fastapi import APIRouter, HTTPException
from data.registrationDB import data

router = APIRouter()


@router.get("/attendees/{email}")
def get_by_email(email):
    attendee = [attendee for attendee in data if attendee["email"] == email]
    if len(attendee) == 0:
        raise HTTPException(status_code=404, detail="Attendee not found")
    else:
        return {"data": attendee[0]}
