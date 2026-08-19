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