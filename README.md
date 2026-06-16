# 💧 Water Demand Forecasting AI

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Framework-000000?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker&logoColor=white)

> **Predicting Tomorrow's Needs, Today.** An AI-driven solution developed during the **Ethiopia AI Institution Program - AI Summer Camp 2024**.

---

## 🌟 The Vision

Water is our most precious resource. This project was born from a simple but powerful question: *How can we use Artificial Intelligence to prevent water scarcity?* 

Developed as a final project for the **AI Summer Camp 2024**, this tool uses Machine Learning to forecast water demand based on temporal patterns, helping communities and governments plan for a sustainable future.

---

## 🧠 How the AI Works

The system uses a **Regression-based Machine Learning model** trained on historical/synthetic water consumption datasets. 

### 🔬 The Prediction Logic:
The model analyzes three core features:
1.  📅 **Year:** Captures long-term population growth and infrastructure trends.
2.  🍂 **Month:** Identifies seasonal changes (dry vs. wet seasons).
3.  ☀️ **Day:** Accounts for monthly usage cycles.

By processing these inputs through a trained Scikit-Learn pipeline, the system outputs the **Expected Water Demand** with high precision.

---

## 🚀 Key Features

- **Intuitive Web UI:** Simple dashboard for quick predictions.
- **Real-Time Inference:** Instant results from the pickled ML model.
- **Containerized Deployment:** Fully Dockerized for "one-click" setup.
- **Future-Ready:** Designed to integrate with regional maps (GIS) and local Ethiopian datasets.

---

## 🛠 Tech Stack

- **Backend:** Flask (Python)
- **AI/ML:** Scikit-Learn, Pandas, NumPy, Pickle
- **Frontend:** HTML5, CSS3, Modern JavaScript
- **DevOps:** Docker, Docker Compose, Poetry

---

## 📂 Repository Structure

```text
├── static/           # CSS & UI Assets
├── templates/        # Flask HTML components
├── app.py            # Main Flask Server & Inference Logic
├── model.pkl         # Pre-trained Scikit-Learn Model
├── Dockerfile        # Container configuration
└── pyproject.toml    # Dependency management
```

---

## ⚙️ Setup & Installation

### Option 1: Docker (Recommended)
```bash
docker compose up -d --build
```
Access at `http://localhost:5001`

### Option 2: Manual Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run server: `python app.py`

---

## 🎓 About the Developer

**Beneyas Tadu**
*   🏆 Developed for the **Ethiopia AI Institution Program**
*   🌟 AI Summer Camp 2024 Finalist
*   🌍 Passionate about using AI for social good and sustainable resource management.

---
*This project is a proof-of-concept for a nationwide water management platform.*
