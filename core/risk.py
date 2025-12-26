def calculate_risk(data):
    score = 0

    if not data['https']['enabled']:
        score += 3

    if len(data['ports']) > 2:
        score += 2

    for v in data['headers'].values():
        if v == "MISSING":
            score += 1

    if score >= 6:
        return "HIGH"
    elif score >= 3:
        return "MEDIUM"
    else:
        return "LOW"
