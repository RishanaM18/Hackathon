import json
from datetime import datetime

def generate_report(text, level, findings):

    report = {
        "date": str(datetime.now()),
        "risk_level": level,
        "total_findings": len(findings),
        "details": findings
    }

    with open("logs/report.json", "w") as f:
        json.dump(report, f, indent=4)

    return report
