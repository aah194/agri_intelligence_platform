import rasterio

with rasterio.open(
    "datasets/sentinel/B04.tif"
) as src:

    window = rasterio.windows.Window(
        0,
        0,
        512,
        512
    )

    red = src.read(
        1,
        window=window
    )

    print(
        red.shape
    )