def evaluate_rules(signals):
    paths = []

    if signals.get("cred_exposures"):
        paths.append({
            "technique": "Credential Exposure via Readable Config Files",
            "impact": "Lateral Movement / Privilege Escalation",
            "reliability": 80,
            "noise": 2,
            "time": 3,
            "why": "Application or system files expose credentials due to weak file permissions.",
            "check": "Manually review flagged files and validate credentials safely."
        })

    return paths
