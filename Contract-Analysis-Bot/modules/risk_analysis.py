def analyze_risk(text):

    risk_keywords = {
        "high": ["penalty", "indemnity", "liable", "termination", "breach"],
        "medium": ["arbitration", "jurisdiction", "renewal", "notice"],
        "low": ["confidentiality", "payment", "service"]
    }

    risk_score = 0
    findings = []

    for word in risk_keywords["high"]:
        if word in text:
            risk_score += 3
            findings.append(f"High Risk Clause Found: {word}")

    for word in risk_keywords["medium"]:
        if word in text:
            risk_score += 2
            findings.append(f"Medium Risk Clause Found: {word}")

    for word in risk_keywords["low"]:
        if word in text:
            risk_score += 1
            findings.append(f"Low Risk Clause Found: {word}")

    if risk_score > 10:
        level = "HIGH"
    elif risk_score > 5:
        level = "MEDIUM"
    else:
        level = "LOW"

    return level, findings
