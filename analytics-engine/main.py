from modules.prediction import PredictionModel

prediction_model = PredictionModel(
    "data/historical_crowd.csv"
)

result = prediction_model.get_prediction_output(
    gate_no="Gate_A",
    gate_capacity=250
)

print(result)