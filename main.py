from fastapi import FastAPI
from app.routes import students, skills, analytics

app = FastAPI(
    title="Student Skills Tracking API",
    description="An API for tracking student skills and progress."
)

app.include_router(students.router, prefix="/students", tags=["Students"])
app.include_router(skills.router, prefix="/skills", tags=["Skills"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])

