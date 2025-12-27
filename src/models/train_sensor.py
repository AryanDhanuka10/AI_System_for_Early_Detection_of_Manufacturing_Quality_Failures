from src.data.sensor_loader import load_sensor_data
from src.models.sensor import SensorAnomalyModel

DATA_DIR = "data/raw/sensors"
MODEL_PATH = "models/sensor/sensor_iforest.pkl"

X, y = load_sensor_data(DATA_DIR)

model = SensorAnomalyModel()
model.train(X)
model.save(MODEL_PATH)

print("✅ Sensor anomaly model trained and saved")
scores = model.predict_score(X)
print("Sample anomaly scores:", scores[:5])
