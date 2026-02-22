from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)             # Dataclass auto-generates init/repr methods; frozen=True makes it immutable (config set once, prevents accidental changes)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: str

@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: str
    output_dir: Path
    num_train_epochs: int
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    warmup_steps: int
    weight_decay: float
    logging_steps: int
    eval_steps: int
    save_steps: int
    gradient_accumulation_steps: int
    report_to: str
    eval_strategy: str
    predict_with_generate: bool
    generation_max_length: int