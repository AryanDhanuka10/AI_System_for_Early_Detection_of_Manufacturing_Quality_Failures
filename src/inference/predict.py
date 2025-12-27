import torch
import cv2
import pandas as pd
import os

from src.inference.model_loader import load_cnn, load_sensor_model
from src.models.ensemble import fuse_scores
from src.inference.uncertainty import is_uncertain
from src.inference.gradcam import GradCAM


cnn = load_cnn()
sensor_model = load_sensor_model()

HITL_DIR = "data/hitl/pending"
os.makedirs(HITL_DIR, exist_ok=True)

def preprocess_image(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = torch.tensor(img, dtype=torch.float32).permute(2, 0, 1).unsqueeze(0)
    return img

def predict(image_path, sensor_csv):
    # CNN prediction
    img = preprocess_image(image_path)
    with torch.no_grad():
        image_prob = cnn(img).item()

    # Sensor anomaly score
    sensor_df = pd.read_csv(sensor_csv)
    features_df = sensor_df.drop(columns=["label"]).mean().to_frame().T
    sensor_score = -sensor_model.score_samples(features_df)[0]


    # Fuse
    final_risk = fuse_scores(image_prob, sensor_score)

    # HITL check
    needs_review = is_uncertain(final_risk)

    if needs_review:
        sensor_df.to_csv(f"{HITL_DIR}/review_{os.path.basename(sensor_csv)}", index=False)

    return {
        "image_defect_prob": round(image_prob, 3),
        "sensor_anomaly_score": round(sensor_score, 3),
        "final_risk_score": round(final_risk, 3),
        "needs_human_review": needs_review
    }

def generate_gradcam(image_tensor, image_path, model):
    cam = GradCAM(model, model.features[-1])
    heatmap = cam.generate(image_tensor)

    img = cv2.imread(image_path)
    img = cv2.resize(img, (heatmap.shape[1], heatmap.shape[0]))

    heatmap = cv2.applyColorMap(np.uint8(255 * heatmap), cv2.COLORMAP_JET)
    overlay = cv2.addWeighted(img, 0.6, heatmap, 0.4, 0)

    output_path = "reports/figures/gradcam_result.png"
    cv2.imwrite(output_path, overlay)
    return output_path