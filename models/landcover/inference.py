from PIL import Image

import torch

from torchvision import transforms

from models.landcover.model import (
    load_model
)

from models.landcover.classes import (
    CLASSES
)

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

model = load_model(
    "saved_models/swin_eurosat.pth"
)


def predict(image_path):

    image = Image.open(
        image_path
    ).convert("RGB")

    image = transform(
        image
    )

    image = image.unsqueeze(0)

    with torch.no_grad():

        outputs = model(
            image
        )

        prediction = torch.argmax(
            outputs,
            dim=1
        )

    return CLASSES[
        prediction.item()
    ]
