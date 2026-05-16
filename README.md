
# 🏭 AI System for Early Detection of Manufacturing Quality Failures

<p align="center">
  <img src="assets/hero_image.png" alt="Manufacturing AI Quality Inspection" width="100%">
</p>

> **Predict defects before they happen. Reduce scrap, rework, and downtime using Hybrid AI.**

---

## 🔗 Project Links
- **GitHub Repository:**  
  https://github.com/AryanDhanuka10/AI_System_for_Early_Detection_of_Manufacturing_Quality_Failures
- **Live Deployed Demo (Frontend):**  
  _[Add Vercel link here]_
- **Backend API (Hugging Face):**  
  _[Add Hugging Face Space link here]_

---

## 📌 Problem Statement

In modern manufacturing environments (automotive, electronics, FMCG, semiconductor):

- Quality defects are often detected **too late**, typically during final inspection
- By that stage, materials are already consumed and rework costs are **5–20× higher**
- Existing systems rely on:
  - Vision-only inspection (misses process drift)
  - Rule-based thresholds (brittle)
  - Manual QA (slow and inconsistent)

### ❌ Core Limitations of Traditional Systems
- No **early warning mechanism**
- No fusion of **images + sensors**
- No uncertainty handling
- No explainability engineers can trust

---

## ✅ Proposed Solution

This project implements a **Hybrid AI Quality Intelligence System** that predicts manufacturing defects **before final inspection** by jointly analyzing:

- 📷 **Product images** (visual defects)
- 📈 **Sensor time-series** (temperature, pressure, vibration)
- 🧠 **Uncertainty-aware decision logic**
- 🧩 **Explainable AI outputs**

The system outputs:
- Defect probability
- Sensor anomaly score
- Final risk score
- Human-in-the-loop (HITL) flag
- Visual and numerical explanations

---

## 🧠 Why Hybrid AI (Not a Single Model / LLM)?

A single model or LLM **cannot** reliably solve this problem.

| Component | Why It’s Needed |
|--------|----------------|
| CNN (Vision) | Detect micro visual anomalies |
| Sensor Anomaly Model | Capture gradual machine drift |
| Ensemble Fusion | Cross-modal reasoning |
| Uncertainty Logic | Safe decision-making |
| Explainability | Trust for engineers |

> **LLMs are not used as decision makers** — this system prioritizes calibrated, explainable, and reliable predictions.

---

## 🏗️ System Architecture

```

Data Ingestion
↓
Preprocessing & Feature Engineering
↓
┌───────────────┐      ┌────────────────┐
│ CNN (Images)  │      │ Sensor Model   │
└───────────────┘      └────────────────┘
↓              ↓
Gated Fusion (Hybrid Risk Engine)
↓
Uncertainty Estimation (Entropy)
↓              ↓
Confident Output   Human-in-the-Loop Queue
↓
Explainability (Grad-CAM + SHAP)
↓
Edge-Optimized Inference (ONNX)

```

---

## 🔬 Models Used

### 1️⃣ Visual Defect Detection
- Custom lightweight **CNN**
- Designed for **edge compatibility**
- Optimized using **ONNX Runtime**

### 2️⃣ Sensor Anomaly Detection
- **Isolation Forest**
- Detects abnormal process behavior
- Robust to unlabeled data

### 3️⃣ Hybrid Risk Fusion
- Gated fusion mechanism
- Sensor anomalies modulate visual confidence
- Produces a calibrated final risk score

---

## 🤖 Human-in-the-Loop (HITL)

When the system is **uncertain**:
- Prediction confidence between 40–60%
- Sample is routed to a **human review queue**
- Enables incremental learning & safer deployment

This reflects **real industrial AI workflows**.

---

## 🔍 Explainable AI (XAI)

### 🖼️ Grad-CAM (Images)
- Highlights **where the model saw the defect**
- Provides visual proof for engineers

### 📊 SHAP (Sensors)
- Shows **which sensor caused the alert**
- Example:
```

Vibration ↑  +0.18
Temperature ↑ +0.07
Pressure ↑ +0.02

```

This turns the system into a **diagnostic tool**, not a black box.

---

## ⚡ Edge Optimization

Factories often run on limited hardware.

- Model converted to **ONNX**
- Inference run via **ONNX Runtime**
- Latency reduced from ~150ms → ~35ms

| Mode | Latency |
|----|--------|
| PyTorch FP32 | ~150 ms |
| ONNX INT8 | ~35 ms |

---

## 📊 Dataset Strategy

### Phase 1 — Synthetic Data (Current)
- Programmatically generated defect images
- Simulated sensor drift
- Enables fast prototyping & pipeline validation

### Phase 2 — Real Industrial Datasets (Planned)
- MVTec Anomaly Detection
- NASA Turbofan Sensor Degradation
- UCI Machine Failure Dataset

> This mirrors how **real AI systems are built in industry**.

---

## 🚀 Deployment

### Backend
- **FastAPI**
- Dockerized
- Deployed on **Hugging Face Spaces**
- Endpoints:
- `/health`
- `/predict`

### Frontend
- Deployed on **Vercel**
- Upload image + sensor CSV
- Displays predictions & explanations

---

## 🛠️ Tech Stack

- **ML/DL:** PyTorch, scikit-learn, XGBoost
- **Explainability:** Grad-CAM, SHAP
- **MLOps:** DVC, MLflow
- **Optimization:** ONNX, ONNX Runtime
- **Backend:** FastAPI
- **Deployment:** Docker, Hugging Face, Vercel

---

## 📈 Business Impact

- Early defect detection → lower scrap & rework
- Reduced false positives via uncertainty-aware inference
- Faster diagnosis through explainability
- Edge-ready for real factory environments

---

## 🧠 Key Takeaways

- Demonstrates **system-level AI thinking**
- Goes beyond model training to **deployment & operations**
- Designed like a **real industrial AI product**

---

## 👤 Author

**Aryan Dhanuka**  
B.Tech | AI / ML / Deep Learning  
GitHub: https://github.com/AryanDhanuka10
---

## ⭐ If you find this project useful
Give it a ⭐ on GitHub — it helps a lot!

---

