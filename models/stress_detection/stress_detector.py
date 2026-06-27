import numpy as np


def detect_stress(ndvi):

    healthy = np.sum(
        ndvi > 0.6
    )

    moderate = np.sum(
        (ndvi >= 0.3) &
        (ndvi <= 0.6)
    )

    stressed = np.sum(
        ndvi < 0.3
    )

    total = ndvi.size

    return {
        "healthy_percent":
        round(
            healthy / total * 100,
            2
        ),

        "moderate_percent":
        round(
            moderate / total * 100,
            2
        ),

        "stressed_percent":
        round(
            stressed / total * 100,
            2
        )
    }