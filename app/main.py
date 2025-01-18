from fastapi import FastAPI
from app.routers import patients, courses, schedules, attendance, payments, notifications
from app.database import engine
from app.models.base import Base

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Clinic Management API", version="1.0.0")

# Routers
app.include_router(patients.router, prefix="/patients", tags=["Patients"])
app.include_router(courses.router, prefix="/courses", tags=["Courses"])
app.include_router(schedules.router, prefix="/schedules", tags=["Schedules"])
app.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
