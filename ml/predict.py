import pandas as pd
import joblib

MODEL_PATH = "ml/risk_model.pkl"

model = joblib.load(MODEL_PATH)

student = pd.DataFrame([{
    "attendance": 55,
    "assignment_avg": 48,
    "quiz_avg": 43,
    "engagement": 35,
    "previous_score": 50
}])

prediction = model.predict(student)[0]
probabilities = model.predict_proba(student)[0]
classes = model.classes_

print("==============================")
print("IRIS RISK PREDICTION")
print("==============================")

print("\nStudent Data:")
print(student.to_string(index=False))

print(f"\nPredicted Risk: {prediction}")

print("\nRisk Probabilities:")

for risk, probability in zip(classes, probabilities):
    print(f"{risk}: {probability:.2%}")