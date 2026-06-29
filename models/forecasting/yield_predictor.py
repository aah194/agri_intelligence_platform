import os
import joblib

MODEL_PATH = "saved_models/yield_model.pkl"

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None


def predict_yield(
    healthy_percent,
    moderate_percent,
    stressed_percent
):

    if model is None:
        return "Yield model unavailable"

    prediction = model.predict(
        [[
            healthy_percent,
            moderate_percent,
            stressed_percent
        ]]
    )[0]

    return f"Predicted Yield: {round(prediction, 2)} tons/hectare"