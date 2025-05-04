from datetime import datetime

def get_mock_residence_data():
    materials = {
        "plastico": {"weight": 120.0, "months": {"Jan": 30, "Feb": 40, "Mar": 50}},
        "papel": {"weight": 80.0, "months": {"Jan": 20, "Feb": 25, "Mar": 35}},
        "vidrio": {"weight": 60.0, "months": {"Jan": 15, "Feb": 20, "Mar": 25}},
        "metal": {"weight": 40.0, "months": {"Jan": 10, "Feb": 15, "Mar": 15}}
    }

    def co2(m, w):
        return w * {"plastico": 0.5, "vidrio": 0.3, "papel": 0.2, "metal": 0.1}[m]

    containers = []
    for mat, data in materials.items():
        containers.append({
            "name": f"{mat.capitalize()} Container",
            "status": "Active",
            "fill_level": 75.0,
            "weight": data["weight"],
            "tokens": data["weight"] * {"plastico": 5, "vidrio": 3, "papel": 2, "metal": 1}[mat],
            "co2_saved": co2(mat, data["weight"])
        })

    total_weight = sum(d["weight"] for d in materials.values())
    total_tokens = sum(c["tokens"] for c in containers)
    total_co2 = sum(c["co2_saved"] for c in containers)

    return {
        "name": "Green Valley Apartments",
        "total_containers": 4,
        "total_weight": total_weight,
        "cycle_tokens": total_tokens,
        "carbon_offset": total_co2,
        "activity_by_material": materials,
        "containers": containers
    }
