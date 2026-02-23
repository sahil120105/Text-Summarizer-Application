# Future Scope & Project Roadmap 🚀

This document outlines the planned enhancements and future directions for the Text Summarizer application to reach industry production standards and improve MLOps maturity.

## 1. MLOps & Experiment Tracking
- **MLflow Integration**: Implement centralized experiment tracking to log hyperparameters, ROUGE scores, and model artifacts.
- **Model Registry**: Version control fine-tuned models and manage their progression from Staging to Production.
- **Weights & Biases (W&B)**: Consider as an alternative for high-fidelity visualization of training metrics.

## 2. Infrastructure & DevOps
- **Containerization**: Complete and optimize the `Dockerfile` for streamlined deployment across diverse environments.
- **CI/CD Pipelines**: Implement GitHub Actions for:
    - Automated testing (unit and integration tests).
    - Continuous deployment to AWS (ECR/App Runner).
- **In-App Training**: Convert the `/train` endpoint to an asynchronous background task with status monitoring.

## 3. Data Management
- **DVC (Data Version Control)**: Track dataset versions and store large artifacts in S3 buckets.
- **Database Integration**: Store processed summaries and user feedback in a production database (e.g., PostgreSQL or MongoDB).

## 4. Model Enhancements
- **Advanced Architectures**: Evaluate larger models like `BART`, `PEGASUS`, or `Llama-3` for improved summarization quality.
- **Automated Retraining**: Implement scheduled retraining pipelines triggered by performance drift or new data availability.
- **Quantization & Distillation**: Optimize model size and inference speed for cost-effective production deployment.

## 5. User Interface & Experience
- **User Feedback Loop**: Add "Thumbs Up/Down" buttons to collect human-in-the-loop data for future fine-tuning.
- **Export Options**: Allow users to download summaries in PDF, Word, or Markdown formats.
- **Multi-lingual Support**: Extend the pipeline to support summarization in multiple languages.

---
*This document serves as a guide for evolving this project from a prototype to a robust production system.*
