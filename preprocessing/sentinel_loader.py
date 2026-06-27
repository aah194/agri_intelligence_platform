import rasterio


def load_band(
    filepath
):

    with rasterio.open(
        filepath
    ) as src:

        band = src.read(1)

    return band