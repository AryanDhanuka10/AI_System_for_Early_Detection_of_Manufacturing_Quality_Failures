import time
import torch
from src.models.cnn import DefectCNN
from src.inference.onnx_infer import onnx_predict
import cv2
import numpy as np

img = cv2.imread("data/raw/images/defect/defect_1.png")
img = cv2.resize(img, (128, 128))
img = img.astype(np.float32) / 255.0
img = torch.tensor(img).permute(2, 0, 1).unsqueeze(0)

# PyTorch
model = DefectCNN()
model.load_state_dict(torch.load("models/cnn/defect_cnn.pt"))
model.eval()

start = time.time()
with torch.no_grad():
    model(img)
torch_time = time.time() - start

# ONNX
start = time.time()
onnx_predict("data/raw/images/defect/defect_1.png")
onnx_time = time.time() - start

print(f"PyTorch latency: {torch_time*1000:.2f} ms")
print(f"ONNX latency: {onnx_time*1000:.2f} ms")
