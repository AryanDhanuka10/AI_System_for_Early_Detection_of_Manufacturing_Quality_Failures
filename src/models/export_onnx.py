import torch
from src.models.cnn import DefectCNN

MODEL_PATH = "models/cnn/defect_cnn.pt"
ONNX_PATH = "models/optimized/defect_cnn.onnx"

model = DefectCNN()
model.load_state_dict(torch.load(MODEL_PATH))
model.eval()

dummy_input = torch.randn(1, 3, 128, 128)

torch.onnx.export(
    model,
    dummy_input,
    ONNX_PATH,
    input_names=["input"],
    output_names=["output"],
    opset_version=11
)

print("✅ CNN exported to ONNX")
