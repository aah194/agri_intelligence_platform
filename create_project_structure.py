import os

folders = [
    "datasets",
    "preprocessing",
    "models",
    "models/landcover",
    "models/stress_detection",
    "models/forecasting",
    "dashboard",
    "notebooks",
    "saved_models"
]

files = [
    "preprocessing/load_data.py",
    "preprocessing/ndvi.py",
    "preprocessing/patch_generator.py",
    "main.py",
    "requirements.txt"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    open(file, "a").close()

print("Project structure created successfully!")