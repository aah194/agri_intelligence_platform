import os
import requests

os.makedirs("datasets/sentinel", exist_ok=True)

files = {
    "B04.tif":
    "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/43/Q/GA/2024/1/S2A_43QGA_20240101_0_L2A/B04.tif",

    "B08.tif":
    "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/43/Q/GA/2024/1/S2A_43QGA_20240101_0_L2A/B08.tif"
}

for filename, url in files.items():

    print(f"Downloading {filename}...")

    response = requests.get(
        url,
        stream=True
    )

    filepath = os.path.join(
        "datasets/sentinel",
        filename
    )

    with open(
        filepath,
        "wb"
    ) as f:

        for chunk in response.iter_content(
            chunk_size=8192
        ):
            f.write(chunk)

    print(
        f"Saved: {filepath}"
    )

print("Download complete.")