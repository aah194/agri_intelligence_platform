import rasterio
import matplotlib.pyplot as plt

from preprocessing.ndvi import (
    calculate_ndvi
)

WINDOW_SIZE = 512

with rasterio.open(
    "datasets/sentinel/B04.tif"
) as red_src:

    red = red_src.read(
        1,
        window=rasterio.windows.Window(
            0,
            0,
            WINDOW_SIZE,
            WINDOW_SIZE
        )
    )

with rasterio.open(
    "datasets/sentinel/B08.tif"
) as nir_src:

    nir = nir_src.read(
        1,
        window=rasterio.windows.Window(
            0,
            0,
            WINDOW_SIZE,
            WINDOW_SIZE
        )
    )

ndvi = calculate_ndvi(
    nir,
    red
)

plt.figure(
    figsize=(8,8)
)

plt.imshow(
    ndvi,
    cmap="RdYlGn"
)

plt.colorbar(
    label="NDVI"
)

plt.title(
    "Real Sentinel-2 NDVI"
)

plt.show()