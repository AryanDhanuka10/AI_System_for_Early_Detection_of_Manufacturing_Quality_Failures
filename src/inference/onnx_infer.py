import onnxruntime as ort
import numpy as np
import cv2

session = ort.InferenceSession(
    "models/optimized/defect_cnn.onnx",
    providers=["CPUExecutionProvider"]
)

def onnx_predict(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (128, 128))
    img = img.astype(np.float32) / 255.0
    img = np.transpose(img, (2, 0, 1))
    img = np.expand_dims(img, axis=0)

    output = session.run(None, {"input": img})
    return float(output[0][0])
