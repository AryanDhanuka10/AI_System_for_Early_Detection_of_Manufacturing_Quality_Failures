import torch
from torch.utils.data import DataLoader
import torch.nn as nn
from src.data.image_loader import DefectDataset
from src.models.cnn import DefectCNN

DATA_DIR = "data/raw/images"
MODEL_PATH = "models/cnn/defect_cnn.pt"

dataset = DefectDataset(DATA_DIR)
loader = DataLoader(dataset, batch_size=16, shuffle=True)

model = DefectCNN()
criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(5):
    total_loss = 0
    for imgs, labels in loader:
        preds = model(imgs).squeeze()
        loss = criterion(preds, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")

torch.save(model.state_dict(), MODEL_PATH)
print("✅ CNN model trained and saved")
