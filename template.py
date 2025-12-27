import os

PROJECT_NAME = "manufacturing_quality_ai"

folders = [
    "data/raw/images",
    "data/raw/sensors",
    "data/processed",
    "data/hitl/pending",
    "models/cnn",
    "models/sensor",
    "models/tabular",
    "models/optimized",
    "reports/figures",
    "notebooks",
    "src/data",
    "src/features",
    "src/models",
    "src/inference",
    "src/api",
    "src/monitoring",
    "src/utils",
    "configs",
    "logs",
    "tests"
]

files = [
    "README.md",
    "requirements.txt",
    "Dockerfile",
    "dvc.yaml",
    ".gitignore",
    "configs/config.yaml",
    "src/api/main.py",
    "src/inference/predict.py",
    "src/models/cnn.py",
    "src/models/sensor.py",
    "src/models/ensemble.py",
    "src/monitoring/drift.py",
    "src/utils/logger.py"
]

def create_structure():
    os.makedirs(PROJECT_NAME, exist_ok=True)
    os.chdir(PROJECT_NAME)

    for f in folders:
        os.makedirs(f, exist_ok=True)

    for file in files:
        open(file, "w").close()

    print("✅ Industry-grade project structure ready")

if __name__ == "__main__":
    create_structure()
