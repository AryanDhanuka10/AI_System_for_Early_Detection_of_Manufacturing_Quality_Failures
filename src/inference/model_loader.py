import torch
import joblib
from src.models.cnn import DefectCNN

CNN_MODEL_PATH = "models/cnn/defect_cnn.pt"
SENSOR_MODEL_PATH = "models/sensor/sensor_iforest.pkl"

def load_cnn():
    model = DefectCNN()
    model.load_state_dict(torch.load(CNN_MODEL_PATH))
    model.eval()
    return model

def load_sensor_model():
    return joblib.load(SENSOR_MODEL_PATH)
