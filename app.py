import streamlit as st
import pandas as pd

from backend.services.risk_service import (
    calculate_risk,
    calculate_score,
    get_risk_factors,
    get_interventions
)


# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="IRIS",
    page_icon="🎓",
    layout="wide"
)


# -----------------------------
# HEADER
# -----------------------------

st.title("IRIS")
st.subheader("Intelligent Risk Identification System")
st.write("Early Academic Risk Detection System")


# -----------------------------
# CSV UPLOAD
# -----------------------------

st.subheader("Student Data")

uploaded_file = st.file_uploader(
    "Upload Student CSV",
    type=["csv"]
)

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    data = pd.read_csv("data/students.csv")


# -----------------------------
# RISK CALCULATION
# -----------------------------

data["risk_level"] = data.apply(
    calculate_risk,
    axis=1
)

data["risk_score"] = data.apply(
    calculate_score,
    axis=1
)

data["risk_factors"] = data.apply(
    lambda row: ", ".join(
        get_risk_factors(row)
    ),
    axis=1
)


# -----------------------------
# DASHBOARD METRICS
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Students",
    len(data)
)

col2.metric(
    "High Risk",
    (data["risk_level"] == "High").sum()
)

col3.metric(
    "Medium Risk",
    (data["risk_level"] == "Medium").sum()
)

col4.metric(
    "Low Risk",
    (data["risk_level"] == "Low").sum()
)


# -----------------------------
# RISK FILTER
# -----------------------------

risk_filter = st.selectbox(
    "Filter Students by Risk",
    ["All", "High", "Medium", "Low"],
    key="risk_filter"
)

if risk_filter == "All":

    filtered_data = data

else:

    filtered_data = data[
        data["risk_level"] == risk_filter
    ]


# -----------------------------
# STUDENT SEARCH
# -----------------------------

search_id = st.text_input(
    "Search Student ID",
    key="student_search"
)

if search_id:

    filtered_data = filtered_data[
        filtered_data["student_id"]
        .astype(str)
        .str.contains(
            search_id,
            case=False,
            na=False
        )
    ]


# -----------------------------
# STUDENT TABLE
# -----------------------------

st.subheader("Student Risk Overview")

st.dataframe(
    filtered_data,
    use_container_width=True
)


# -----------------------------
# STUDENT RISK ANALYSIS
# -----------------------------

st.subheader("Student Risk Analysis")

if not filtered_data.empty:

    selected_student = st.selectbox(
        "Select Student",
        filtered_data["student_id"].tolist(),
        key="student_selector"
    )

    student = filtered_data[
        filtered_data["student_id"] == selected_student
    ].iloc[0]


    # -------------------------
    # RISK SCORE & LEVEL
    # -------------------------

    col1, col2 = st.columns(2)

    col1.metric(
        "Risk Score",
        student["risk_score"]
    )

    col2.metric(
        "Risk Level",
        student["risk_level"]
    )


    # -------------------------
    # RISK FACTORS
    # -------------------------

    st.write("### Risk Factors")

    risk_factors = get_risk_factors(student)

    if risk_factors:

        for factor in risk_factors:

            st.warning(
                f"⚠️ {factor}"
            )

    else:

        st.success(
            "No major risk factors detected."
        )


    # -------------------------
    # INTERVENTION
    # -------------------------

    st.write("### Recommended Interventions")

    interventions = get_interventions(student)

    for intervention in interventions:

        st.info(
            f"💡 {intervention}"
        )


else:

    st.warning(
        "No students match the selected filters."
    )


# -----------------------------
# RISK DISTRIBUTION
# -----------------------------

st.subheader("Risk Distribution")

risk_counts = data[
    "risk_level"
].value_counts()

st.bar_chart(
    risk_counts
)