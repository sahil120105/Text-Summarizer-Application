# Project Structure Guide

This document provides an overview of the Text Summarizer Application's project structure. It is intended to help new contributors understand the codebase and to serve as a reference for future development.

## 📂 Root Directory

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

## 🏗️ Source Code Structure (`src/textSummarizer`)

The core logic resides in `src/textSummarizer`. It follows a modular, pipeline-based architecture.

| Module | Description |
| :--- | :--- |
| `components/` | Contains the implementation of individual stages (e.g., Data Ingestion, Transformation, Training). |
| `config/` | Configuration management (loading `config.yaml`, `params.yaml`). |
| `constants/` | Defines project-wide constants. |
| `entity/` | Data classes (dataclasses) for type safety and structured configuration. |
| `logging/` | Custom logging configuration. |
| `pipeline/` | Orchestrates the execution of components in stages. |
| `utils/` | Common utility functions (e.g., file handling, parsing). |

## 🔄 Development Workflow

Follow these steps for implementing new features or stages in the pipeline. This ensures consistency and reproducibility across the project.

1.  **Update `config.yaml`**
    *   Add or modify configuration settings in `config/config.yaml`. This is where file paths, source URLs, and other constant settings for the new stage should be defined.

2.  **Update `params.yaml`**
    *   Add or modify model hyperparameters or training settings in `params.yaml`. Keep all tunable parameters here to experiment easily without changing source code.

3.  **Update Entity**
    *   Update `src/textSummarizer/entity/__init__.py`.
    *   Define the return type (schema) of the configuration manager functions using Python `dataclasses` (frozen). This ensures type safety and that the configuration object is immutable.

4.  **Update the Configuration Manager in `src/config`**
    *   Update `src/textSummarizer/config/configuration.py`.
    *   Implement methods to read the updated `config.yaml`, `params.yaml`, and `schema.yaml`.
    *   Return the corresponding entity dataclass created in the previous step.

5.  **Update the Components**
    *   Create or update components in `src/textSummarizer/components/`.
    *   This is where the core logic of the stage resides (e.g., specific logic for `DataIngestion`, `ModelTrainer`).
    *   The component should accept the configuration entity and perform the required operations.

6.  **Update the Pipeline**
    *   Create or update the pipeline stage in `src/textSummarizer/pipeline/` (e.g., `stage_0x_name.py`).
    *   Initialize the `ConfigurationManager` and the specific `Component`.
    *   Define a `main` method to orchestrate the execution of the component.

7.  **Update `main.py`**
    *   Import the new pipeline stage in `main.py`.
    *   Add the execution of the new stage to the main execution flow, ensuring it runs in the correct order.

8.  **Update `app.py`**
    *   If the changes encompass new endpoints or UI features, update `app.py`.
    *   Ensure the API routes or Streamlit/Flask interface reflects the new capabilities of the pipeline.

## 📝 Key Files

*   **`config/config.yaml`**: Central configuration for artifacts, data paths, and model parameters.
*   **`main.py`**: Runs the defined pipeline stages sequentially.
*   **`src/textSummarizer/pipeline/stage01_data_ingestion.py`**: Example of a pipeline stage.
*   **`src/textSummarizer/components/data_ingestion.py`**: Logic for downloading and extracting data.

---
*This document should be updated as new features and directories are added.*
