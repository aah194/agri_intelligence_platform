import numpy as np

def calculate_ndvi(
    nir_band,
    red_band
):

    nir_band = nir_band.astype(
        np.float32
    )

    red_band = red_band.astype(
        np.float32
    )

    ndvi = (
        nir_band - red_band
    ) / (
        nir_band + red_band + 1e-10
    )

    return ndvi