import numpy as np
import matplotlib.pyplot as plt

from preprocessing.ndvi import (
    calculate_ndvi
)

nir = np.array([
    [200,180,220],
    [220,210,230],
    [250,240,255]
])

red = np.array([
    [100,120,140],
    [140,130,150],
    [160,170,180]
])

ndvi = calculate_ndvi(
    nir,
    red
)

plt.imshow(
    ndvi,
    cmap="RdYlGn"
)

plt.colorbar(
    label="NDVI"
)

plt.title(
    "NDVI Visualization"
)

plt.show()