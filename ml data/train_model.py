import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ============================================================
# 1. LOAD DATASET
# ============================================================

DATASET_PATH = "ml data/dataset.csv"

df = pd.read_csv(DATASET_PATH)

print("Dataset loaded successfully!")
print(f"Total students: {len(df)}")


# ============================================================
# 2. DEFINE FEATURES AND TARGET
# ============================================================

features = [
    "attendance",
    "assignment_avg",
    "quiz_avg",
    "engagement",
    "previous_score"
]

X = df[features]
y = df["risk"]


# ============================================================
# 3. SPLIT DATA
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print(f"\nTraining samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")


# ============================================================
# 4. CREATE RANDOM FOREST MODEL
# ============================================================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)


# ============================================================
# 5. TRAIN MODEL
# ============================================================

print("\nTraining Random Forest model...")

model.fit(X_train, y_train)

print("Model training completed!")


# ============================================================
# 6. MAKE PREDICTIONS
# ============================================================

y_pred = model.predict(X_test)


# ============================================================
# 7. MODEL EVALUATION
# ============================================================

accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("MODEL PERFORMANCE")
print("==============================")

print(f"Accuracy: {accuracy:.2%}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# ============================================================
# 8. FEATURE IMPORTANCE
# ============================================================

print("\n==============================")
print("FEATURE IMPORTANCE")
print("==============================")

importance = pd.DataFrame({
    "feature": features,
    "importance": model.feature_importances_
})

importance = importance.sort_values(
    by="importance",
    ascending=False
)

print(importance)


# ============================================================
# 9. SAVE MODEL
# ============================================================

MODEL_PATH = "ml data/risk_model.pkl"

joblib.dump(model, MODEL_PATH)

print("\n==============================")
print("MODEL SAVED SUCCESSFULLY")
print("==============================")

print(f"Saved to: {MODEL_PATH}")