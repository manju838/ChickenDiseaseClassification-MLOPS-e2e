from dataclasses import dataclass
from pathlib import Path

# Entity defines custom data types/return types.
# Here, DataIngestion related paths are defined in config.yaml and is checked with DataIngestionConfig

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path