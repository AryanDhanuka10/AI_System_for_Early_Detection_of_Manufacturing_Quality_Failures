import shap
import pandas as pd

def explain_sensor(sensor_model, train_data, sample):
    explainer = shap.TreeExplainer(sensor_model)
    shap_values = explainer.shap_values(sample)

    explanation = dict(
        zip(sample.columns, shap_values[0])
    )
    return explanation
