from modules.realtime import RealtimeProcessor
from modules.capacity import CapacityModel
from modules.risk import RiskModel
from modules.prediction import PredictionModel
from modules.alerts import AlertSystem


# ----------------------------
# INPUT FROM CV TEAM
# ----------------------------

input_data = {
    "timestamp": "2026-08-28T18:30:00",
    "crowd_number": 180,
    "gate_no": "Gate_A",
    "density": "high"
}


# ----------------------------
# REALTIME
# ----------------------------

realtime = RealtimeProcessor()

clean_data = realtime.process(input_data)


# ----------------------------
# CAPACITY
# ----------------------------

capacity_model = CapacityModel(
    "data/gate_capacity.csv"
)

capacity_result = (
    capacity_model.calculate_capacity_utilization(
        clean_data["crowd_number"],
        clean_data["gate_no"]
    )
)


# ----------------------------
# RISK
# ----------------------------

risk_model = RiskModel()

risk_result = risk_model.calculate_risk(
    capacity_result["capacity_utilization"]
)


# ----------------------------
# PREDICTION
# ----------------------------

prediction_model = PredictionModel(
    "data/historical_crowd.csv"
)

gate_capacity = capacity_model.get_gate_capacity(
    clean_data["gate_no"]
)

prediction_result = (
    prediction_model.get_prediction_output(
        clean_data["gate_no"],
        gate_capacity
    )
)

alert_system = AlertSystem()

alerts_result = alert_system.generate_alerts(
    zone=clean_data["gate_no"],
    risk=risk_result,
    congestion_probability=
        prediction_result["congestion_probability"]
)


# ----------------------------
# TEMPORARY FINAL OUTPUT
# ----------------------------

final_output = {

    "zone": clean_data["gate_no"],

    "capacity_utilization":
        capacity_result["capacity_utilization"],

    "risk":
        risk_result,

    "predicted_crowd":
        prediction_result["predicted_crowd"],

    "prediction_window":
        prediction_result["prediction_window"],

    "congestion_probability":
        prediction_result["congestion_probability"],

    "alerts": alerts_result,

    "internal_rerouting": {},

    "external_recommendations": {},

    "recommended_visit_time":
        None,

    "recommended_action":
        None
}

print(final_output)