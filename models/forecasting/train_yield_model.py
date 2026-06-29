import pandas as pd

from sklearn.ensemble import (
    RandomForestRegressor
)

import joblib


data = pd.read_csv(
    "datasets/yield_data.csv"
)

X = data[
    [
        "healthy",
        "moderate",
        "stressed"
    ]
]

y = data[
    "yield"
]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(
    X,
    y
)

joblib.dump(
    model,
    "saved_models/yield_model.pkl"
)

print(
    "Yield model saved successfully"
)