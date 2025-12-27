import os

PROJECT_NAME = "manufacturing_quality_ai"

structure = [
    "data/raw",
    "data/processed",
    "data/external",
    "models",
    "notebooks",
    "src/data",
    "src/features",
    "src/models",
    "src/inference",
    "src/api",
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
    "src/__init__.py",
    "src/data/data_loader.py",
    "src/features/feature_engineering.py",
    "src/models/cnn_model.py",
    "src/models/time_series_model.py",
    "src/models/tabular_model.py",
    "src/models/ensemble.py",
    "src/inference/predict.py",
    "src/api/main.py",
    "src/utils/logger.py",
    "configs/config.yaml"
]

def create_project():
    os.makedirs(PROJECT_NAME, exist_ok=True)
    os.chdir(PROJECT_NAME)

    for folder in structure:
        os.makedirs(folder, exist_ok=True)

    for file in files:
        with open(file, "w") as f:
            f.write("")

    print("✅ Project structure created successfully")

if __name__ == "__main__":
    create_project()
