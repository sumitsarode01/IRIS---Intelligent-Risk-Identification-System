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


def calculate_score(row):
    score = (
        row["attendance"] * 0.35
        + row["assignment_avg"] * 0.25
        + row["quiz_avg"] * 0.20
        + row["engagement"] * 0.20
    )

    return round(score, 2)


def get_risk_factors(row):
    factors = []

    if row["attendance"] < 60:
        factors.append("Low attendance")

    if row["assignment_avg"] < 60:
        factors.append("Low assignment performance")

    if row["quiz_avg"] < 50:
        factors.append("Low quiz performance")

    if row["engagement"] < 50:
        factors.append("Low engagement")

    return factors


def get_interventions(row):
    interventions = []

    if row["attendance"] < 60:
        interventions.append(
            "Create an attendance improvement plan"
        )

    if row["assignment_avg"] < 60:
        interventions.append(
            "Provide assignment support and follow-up"
        )

    if row["quiz_avg"] < 50:
        interventions.append(
            "Provide additional quiz preparation or tutoring"
        )

    if row["engagement"] < 50:
        interventions.append(
            "Schedule mentoring and increase student engagement"
        )

    if not interventions:
        interventions.append(
            "Continue regular academic monitoring"
        )

    return interventions