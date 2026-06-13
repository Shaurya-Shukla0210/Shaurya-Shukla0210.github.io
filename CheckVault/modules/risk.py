def calculate_risk(metadata):

    risk = 0
    reasons = []

    if metadata.get("exif_present") == False:
        risk += 20
        reasons.append("No EXIF metadata found")

    if risk <= 20:
        level = "Low Risk"
    elif risk <= 50:
        level = "Medium Risk"
    else:
        level = "High Risk"

    return {
        "risk_score": risk,
        "risk_level": level,
        "reasons": reasons
    }