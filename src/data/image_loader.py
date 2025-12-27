import os
import cv2
import torch
from torch.utils.data import Dataset

class DefectDataset(Dataset):
    def __init__(self, root_dir):
        self.samples = []
        for label, cls in enumerate(["good", "defect"]):
            cls_path = os.path.join(root_dir, cls)
            for img in os.listdir(cls_path):
                self.samples.append((os.path.join(cls_path, img), label))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        path, label = self.samples[idx]
        img = cv2.imread(path)
        img = cv2.resize(img, (128, 128))
        img = img / 255.0
        img = torch.tensor(img, dtype=torch.float32).permute(2, 0, 1)
        return img, torch.tensor(label, dtype=torch.float32)
