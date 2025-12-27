from sklearn.ensemble import IsolationForest
import joblib

class SensorAnomalyModel:
    """
    Detects abnormal machine behavior using sensor statistics.
    """
    def __init__(self):
        self.model = IsolationForest(
            n_estimators=100,
            contamination=0.3,
            random_state=42
        )

    def train(self, X):
        self.model.fit(X)

    def predict_score(self, X):
        # Higher score = more anomalous
        return -self.model.score_samples(X)

    def save(self, path):
        joblib.dump(self.model, path)

    def load(self, path):
        self.model = joblib.load(path)
