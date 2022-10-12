import fastapi
import uvicorn
from routers import getAttendeeByEmail, registerAttendee, getAllAttendees


app = fastapi.FastAPI()


@app.get("/")
def index():
    return {"message": "welcome to the PyConGhana Registration App"}


app.include_router(registerAttendee.router)
app.include_router(getAttendeeByEmail.router)
app.include_router(getAllAttendees.router)

if __name__ == "__main__":
    uvicorn.run(app)
