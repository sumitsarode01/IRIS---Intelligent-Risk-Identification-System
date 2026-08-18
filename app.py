import streamlit as st
import pandas as pd

st.title("IRIS")
st.subheader("Intelligent Risk Identification System")

st.write("Early Academic Risk Detection System")

data = pd.read_csv("data/students.csv")

def calculate_risk(row):
    score = (
        row["attendance"] * 0.35
        + row["assignment_avg"] * 0.25
        + row["quiz_avg"] * 0.20
        + row["engagement"] * 0.20
    )

    if score < 50:
        return "High"
    elif score < 70:
        return "Medium"
    else:
        return "Low"


data["risk_level"] = data.apply(calculate_risk, axis=1)

st.write("Risk Analysis")
st.dataframe(data)