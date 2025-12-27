import numpy as np
import pandas as pd
import os

OUTPUT_DIR = "data/raw/sensors"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_sensor_sample(defect=False, n=200):
    temperature = np.random.normal(70, 2, n)
    pressure = np.random.normal(30, 1, n)
    vibration = np.random.normal(0.02, 0.005, n)

    if defect:
        vibration += np.linspace(0, 0.05, n)
        temperature += np.linspace(0, 5, n)

    return pd.DataFrame({
        "temperature": temperature,
        "pressure": pressure,
        "vibration": vibration,
        "label": int(defect)
    })

for i in range(50):
    df = generate_sensor_sample(defect=False)
    df.to_csv(f"{OUTPUT_DIR}/normal_{i}.csv", index=False)

for i in range(50):
    df = generate_sensor_sample(defect=True)
    df.to_csv(f"{OUTPUT_DIR}/defect_{i}.csv", index=False)

print("✅ Sensor data generated")
