import timm
import torch


def load_model(model_path):

    model = timm.create_model(
        "swin_tiny_patch4_window7_224",
        pretrained=False,
        num_classes=10
    )

    model.load_state_dict(
        torch.load(
            model_path,
            map_location=torch.device("cpu")
        )
    )

    model.eval()

    return model