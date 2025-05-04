from collections import defaultdict
from datetime import datetime

def mock_stats(containers):
    today_weight = sum(c["weight"] for c in containers)
    materials = {
        "plastico": 0.5,
        "vidrio": 0.3,
        "papel": 0.2,
        "metal": 0.1
    }

    co2 = 0
    for c in containers:
        for m in c["materials"]:
            co2 += c["weight"] * materials.get(m, 0)

    return {
        "today": {"weight": today_weight, "containers": len(containers)},
        "week": {"weight": today_weight * 3.5, "containers": len(containers)},  # Mocked
        "carbon_monthly": {"co2_saved": round(co2, 2)}
    }
