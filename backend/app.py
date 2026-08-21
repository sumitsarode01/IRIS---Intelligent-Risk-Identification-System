from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.services.risk_service import calculate_risk

app = FastAPI(
    title="IRIS API",
    description="Intelligent Risk Identification System Backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "IRIS Backend is running",
        "status": "success"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "IRIS Backend"
    }


@app.post("/api/risk")
def predict_risk(student: dict):
    risk_level = calculate_risk(student)

    return {
        "student_id": student.get("student_id"),
        "risk_level": risk_level
    }