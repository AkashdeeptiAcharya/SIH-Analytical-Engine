from modules.capacity import CapacityModel
from modules.risk import RiskModel

capacity_model = CapacityModel(
    "data/gate_capacity.csv"
)

risk_model = RiskModel()

capacity_result = (
    capacity_model.calculate_capacity_utilization(
        crowd_number=180,
        gate_no="Gate_A"
    )
)

risk_result = risk_model.calculate_risk(
    capacity_result["capacity_utilization"]
)

print("Capacity:", capacity_result)
print("Risk:", risk_result)