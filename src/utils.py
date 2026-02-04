def kpi_status(actual, target):
    if actual >= target:
        return "On track"
    if actual >= 0.9 * target:
        return "Slightly behind"
    return "At risk"


def percent_change(current, previous):
    if previous == 0:
        return None
    return ((current - previous) / previous) * 100
