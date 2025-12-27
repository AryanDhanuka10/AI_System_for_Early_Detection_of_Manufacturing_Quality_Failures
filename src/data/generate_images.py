import cv2
import numpy as np
import os

GOOD_DIR = "data/raw/images/good"
DEFECT_DIR = "data/raw/images/defect"

os.makedirs(GOOD_DIR, exist_ok=True)
os.makedirs(DEFECT_DIR, exist_ok=True)

def generate_good_image(i):
    img = np.ones((128, 128, 3), dtype=np.uint8) * 200
    cv2.imwrite(f"{GOOD_DIR}/good_{i}.png", img)

def generate_defect_image(i):
    img = np.ones((128, 128, 3), dtype=np.uint8) * 200
    x1, y1 = np.random.randint(10, 100, size=2)
    x2, y2 = x1 + np.random.randint(10, 20), y1 + np.random.randint(10, 20)
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 0), 2)
    cv2.imwrite(f"{DEFECT_DIR}/defect_{i}.png", img)

for i in range(100):
    generate_good_image(i)
    generate_defect_image(i)

print("✅ Image data generated")
