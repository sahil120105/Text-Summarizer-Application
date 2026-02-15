from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)             # Dataclass auto-generates init/repr methods; frozen=True makes it immutable (config set once, prevents accidental changes)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path