import numpy as np

from preprocessing.ndvi import (
    calculate_ndvi
)

nir = np.array([
    [200, 180],
    [220, 210]
])

red = np.array([
    [100, 120],
    [140, 130]
])

ndvi = calculate_ndvi(
    nir,
    red
)

print(ndvi)