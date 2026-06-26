from models.landcover.inference import (
    predict
)

result = predict(
    "test_image.jpg"
)

print(result)