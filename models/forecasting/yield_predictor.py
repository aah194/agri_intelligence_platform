def predict_yield(
    healthy,
    moderate,
    stressed
):

    score = (
        healthy * 1.0 +
        moderate * 0.5 -
        stressed * 1.0
    )

    if score > 80:

        return "High Yield Expected"

    elif score > 40:

        return "Moderate Yield Expected"

    else:

        return "Low Yield Expected"