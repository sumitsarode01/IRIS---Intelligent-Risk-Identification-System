import numpy as np
import pandas as pd

np.random.seed(42)

n_students = 500

attendance = np.random.randint(40, 101, n_students)
assignment_avg = np.random.randint(30, 101, n_students)
quiz_avg = np.random.randint(25, 101, n_students)
engagement = np.random.randint(20, 101, n_students)
previous_score = np.random.randint(30, 101, n_students)

risk_score = (
    (100 - attendance) * 0.30
    + (100 - assignment_avg) * 0.20
    + (100 - quiz_avg) * 0.20
    + (100 - engagement) * 0.15
    + (100 - previous_score) * 0.15
)

risk_score += np.random.normal(0, 4, n_students)

risk = np.where(
    risk_score >= 55,
    "High",
    np.where(risk_score >= 35, "Medium", "Low")
)

df = pd.DataFrame({
    "attendance": attendance,
    "assignment_avg": assignment_avg,
    "quiz_avg": quiz_avg,
    "engagement": engagement,
    "previous_score": previous_score,
    "risk": risk
})

df.to_csv("ml/dataset.csv", index=False)

print("Dataset generated successfully!")
print(f"Total students: {len(df)}")
print("\nRisk distribution:")
print(df["risk"].value_counts())
print("\nSaved to: ml/dataset.csv")