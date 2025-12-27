def fuse_scores(image_prob, sensor_score):
    """
    Combines vision probability and sensor anomaly score.
    Sensor score modulates visual confidence.
    """

    # Normalize sensor score (simple heuristic)
    sensor_weight = min(sensor_score / 1.0, 1.0)

    final_risk = image_prob * (1 + sensor_weight)

    # Clamp to [0, 1]
    final_risk = min(final_risk, 1.0)

    return final_risk
