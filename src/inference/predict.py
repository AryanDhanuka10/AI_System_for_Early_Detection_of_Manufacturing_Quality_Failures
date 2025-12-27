import torch
import cv2
import pandas as pd
import os

from src.inference.model_loader import load_cnn, load_sensor_model
from src.models.ensemble import fuse_scores
from src.inference.uncertainty import is_uncertain

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
    features = sensor_df.drop(columns=["label"]).mean().values.reshape(1, -1)
    sensor_score = -sensor_model.score_samples(features)[0]

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
