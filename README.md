# Fine-tuning T5 for Abstractive Text Summarization on SAMSum Dataset

A modular, production-ready NLP application that manages the full lifecycle of fine-tuning and deploying a Google T5 (Small) model for high-quality dialogue summarization.

---

## 🚀 Overview

This project implements an end-to-end MLOps workflow designed for reproducible machine learning. By leveraging a stage-based architecture, it decouples data management, model optimization, and deployment, making it ideal for scalable NLP solutions.

### 💻 Tech Stack
*   **AI/ML**: Python, PyTorch, Hugging Face Transformers, Hugging Face Datasets, Evaluate (ROUGE).
*   **Backend**: FastAPI, Uvicorn, Jinja2.
*   **DevOps**: Docker, GitHub Actions (CI/CD).
*   **Cloud**: Amazon Web Services (EC2, ECR).
*   **Infrastructure**: Configuration-driven (YAML), Modular Pipeline Architecture.

---

## 🏗️ Technical Pipeline Architecture

The application is structured into discrete, independent modules coordinated by a central configuration manager.

### Pipeline Stage Details

| Stage | Technical Implementation |
| :--- | :--- |
| **Data Ingestion** | Automated retrieval of the SAMSum dataset (zip) from remote storage, followed by checksum validation and extraction into organized directory structures. |
| **Data Validation** | Manifest-based integrity checks. It verifies the presence and schema of `train.csv`, `test.csv`, and `validation.csv` to prevent downstream failures. |
| **Data Transformation** | Parallel tokenization using T5's SentencePiece tokenizer. It converts text and dialogue into input-target tensor pairs with specialized padding and max-length constraints (Target: 128, Input: 1024). |
| **Model Training** | Fine-tuning via the Hugging Face `Trainer` API. Employs gradient accumulation (step=16) and weight decay (0.01) to optimize performance for lower-memory environments. |
| **Model Evaluation** | Post-training assessment using the ROUGE metric. Calculates overlaps between generated summaries and ground truth sequences to ensure semantic consistency. |
| **Inference/Prediction** | An optimized prediction wrapper that handles model loading (from local artifacts) and manages the full tokenization-generation-decoding loop for live requests. |

---

## 📊 Dataset & Metrics

### SAMSum Dataset
The project utilizes the **SAMSum dataset**, which consists of approximately **16,000 messenger-like dialogues** with corresponding human-written summaries. Unlike standard news summarization, this dataset requires the model to handle conversational informalities, emojis, and multi-turn exchanges, providing a rigorous test for abstractive summarization capabilities.

### Final Training Results
The model reached its optimal performance at step 800 during the fine-tuning process:

| Metric | Value |
| :--- | :--- |
| **Validation Loss** | 1.6829 |
| **Rouge1** | 42.7613 |
| **Rouge2** | 20.2532 |
| **RougeL** | 36.1324 |
| **RougeLsum** | 39.5476 |
| **Gen Len** | 19.2714 |

---

## 🛠️ Usage & Execution

### 1. Environment Setup
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Execution Flow
*   **To run the full pipeline (Ingestion to Evaluation)**:
    ```bash
    python main.py
    ```
*   **To launch the web interface locally**:
    ```bash
    python app.py
    ```
    Visit `http://localhost:8000` to interact with the summarizer.

### 3. Docker Deployment
```bash
docker build -t text-summarizer .
docker run -p 8000:8000 text-summarizer
```

---

## ☁️ Cloud Deployment (CI/CD)

The project includes an integrated CI/CD workflow for **AWS Deployment**:
*   **Registry**: Amazon ECR (Elastic Container Registry).
*   **Compute**: Amazon EC2 with self-hosted runner.
*   **Pipeline**: GitHub Actions triggers builds and deployments on every push to main.

---

## 📁 Project Organization
```text
.
├── artifacts/          # Versioned ML datasets and fine-tuned models
├── config/             # YAML configurations
├── src/                # Modular source code
│   └── textSummarizer/ # Core package logic
├── research/           # Jupyter Notebooks for EDA
├── app.py              # FastAPI server
└── main.py             # Pipeline orchestration engine
```