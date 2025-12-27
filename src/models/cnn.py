import torch.nn as nn
import torch

class DefectCNN(nn.Module):
    """
    Simple CNN for binary defect detection.
    Lightweight for edge deployment later.
    """
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 16, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(16, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(32 * 32 * 32, 1)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return torch.sigmoid(x)
