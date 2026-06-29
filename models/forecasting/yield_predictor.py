import joblib


model = joblib.load(
    "saved_models/yield_model.pkl"
)


def predict_yield(
    healthy,
    moderate,
    stressed
):

    prediction = model.predict(
        [[
            healthy,
            moderate,
            stressed
        ]]
    )[0]

    return round(
        prediction,
        2
    )