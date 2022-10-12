from fastapi import APIRouter
from data.registrationDB import data


router = APIRouter()


@router.get("/attendees")
def get_attendees():
    if len(data) == 0:
        return {"message": "no attendees registered yet"}
    else:
        return {"data": data}
