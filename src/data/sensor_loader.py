import pandas as pd
import os

def load_sensor_data(folder):
    data = []
    labels = []

    for file in os.listdir(folder):
        df = pd.read_csv(os.path.join(folder, file))
        features = df.drop(columns=["label"]).mean().values
        label = df["label"].iloc[0]

        data.append(features)
        labels.append(label)

    return pd.DataFrame(data, columns=["temperature", "pressure", "vibration"]), labels
