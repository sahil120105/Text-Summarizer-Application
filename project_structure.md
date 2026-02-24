# Project Structure Guide

This document provides an overview of the Text Summarizer Application's project structure. It is intended to help new contributors understand the codebase and to serve as a reference for future development.

## ðŸ“‚ Root Directory

| File/Directory | Description |
| :--- | :--- |
| `.github/` | Contains GitHub Actions workflows for CI/CD. |
| `config/` | Configuration files for the application. |
| `research/` | Jupyter notebooks for experimentation and trials. |
| `src/` | Source code for the application. |
| `venv/` | Python virtual environment. |
| `artifacts/` | Stores generated artifacts (datasets, models, etc.) from the pipeline. |
| `app.py` | Entry point for the web application (Flask/Streamlit/FastAPI). |
| `main.py` | Main entry point for running the training/pipeline. |
| `params.yaml` | Hyperparameters and model configuration. |
| `requirements.txt` | Python dependencies. |
| `setup.py` | Setup script for packaging the application as a Python library. |
| `template.py` | Utility script for project initialization or templating. |

## ðŸ—ï¸ Source Code Structure (`src/textSummarizer`)

The core logic resides in `src/textSummarizer`. It follows a modular, pipeline-based architecture.

| Module | Description |
| :--- | :--- |
| `components/` | Contains the implementation of individual stages (e.g., Data Ingestion, Transformation, Training). |
| `config/` | Configuration management (loading `config.yaml`, `params.yaml`). |
| `constants/` | Defines project-wide constants. |
| `entity/` | Data classes (dataclasses) for type safety and structured configuration. |
| `logging/` | Custom logging configuration. |
| `pipeline/` | Orchestrates the execution of components in stages (e.g., training, prediction). |
| `utils/` | Common utility functions (e.g., file handling, parsing). |

## ðŸ”„ Development Workflow

Follow these steps for implementing new features or stages in the pipeline (e.g., adding `PredictionPipeline`).

1.  **Update `config.yaml`**
    *   Add configuration settings in `config/config.yaml` (e.g., `prediction` section with model paths).

2.  **Update Entity**
    *   Update `src/textSummarizer/entity/__init__.py`.
    *   Define the dataclass (e.g., `PredictionConfig`) for type safety.

3.  **Update Configuration Manager**
    *   Update `src/textSummarizer/config/configuration.py`.
    *   Implement getter methods (e.g., `get_prediction_config`).

4.  **Create Pipeline**
    *   Create the stage in `src/textSummarizer/pipeline/` (e.g., `prediction.py`).
    *   Implement the core logic or inference flow.

5.  **Update `main.py`**
    *   Import and execute the new stage in `main.py` for CLI-based execution and verification.

## ðŸ“ Key Files

*   **`config/config.yaml`**: Central configuration for artifacts, data paths, and model parameters.
*   **`main.py`**: Sequentially runs pipeline stages (Data Ingestion -> Validation -> Transformation -> Training -> Prediction).
*   **`src/textSummarizer/pipeline/prediction.py`**: Handles model inference and summary generation.
*   **`artifacts/model_trainer/t5_samsum_model/`**: Contains the fine-tuned model and tokenizer.

---
*This document should be updated as new features and directories are added.*
