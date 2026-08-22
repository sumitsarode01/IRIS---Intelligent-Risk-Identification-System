from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="IRIS Backend")

MODEL_PATH = "ml/risk_model.pkl"
model = joblib.load(MODEL_PATH)


class StudentData(BaseModel):
    attendance: float
    assignment_avg: float
    quiz_avg: float
    engagement: float
    previous_score: float


@app.get("/")
def home():
    return {"message": "IRIS Backend is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict_risk(student: StudentData):
    data = pd.DataFrame([{
        "attendance": student.attendance,
        "assignment_avg": student.assignment_avg,
        "quiz_avg": student.quiz_avg,
        "engagement": student.engagement,
        "previous_score": student.previous_score
    }])

    prediction = model.predict(data)[0]
    probabilities = model.predict_proba(data)[0]

    risk_probabilities = {}

    for risk, probability in zip(model.classes_, probabilities):
        risk_probabilities[risk] = round(float(probability), 4)

    return {
        "predicted_risk": prediction,
        "risk_probabilities": risk_probabilities
    }