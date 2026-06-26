import numpy as np


def calculate_ndvi(
    red_band,
    nir_band
):

    red = red_band.astype(
        np.float32
    )

    nir = nir_band.astype(
        np.float32
    )

    ndvi = (
        nir - red
    ) / (
        nir + red + 1e-10
    )

    return ndvi