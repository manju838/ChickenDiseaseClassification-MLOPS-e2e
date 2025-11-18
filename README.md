# ChickenDiseaseClassification-MLOPS-e2e
Follows https://www.youtube.com/watch?v=p1bfK8ZJgkE

## Steps

1) To create a fresh repo with the MLOPS template: 
```bash
python template.py
```

2) To install this project:
```bash
$conda create -n chicken python=3.10 pip
$conda activate chicken

#Make sure:
$which pip
/c/Users/manju/.conda/envs/chicken/Scripts/pip
# Failing this means pip is not using/pointed to isolated env completely and can cause package version conflict issues with random packages in your laptop.

$pip install -r requirements.txt
```

1) DataIngestion: 
A) Primary Code: The code that directly does the task(here downloading and extracting data)
- Purpose: Get raw data from source URL and place it in designated location in project workspace. 
- Tasks: Download compressed data and extracting it into specific location in workspace.
- Location: DataIngestion is part/component of project workflow, so it is present in ```src/{project_name}/components/data_ingestion.py```

B) Secondary Code: Feeds input and output formats, supports, configures, and triggers the primary code.
- Input: Present in ```config/config.yaml```. Supplies the info: a) where is the rootdir? b) where is the dataset src? c) where to download? d) where to unzip?
- Output: Define the input datatype from DataIngestion process, using DataIngestionConfig dataclass(a class that doesnt need __init__ fn.). Present in ```src/{project_name}/entity/config_entity.py```
- ConfigurationManager: Bridging code that reads ```config/config.yaml``` to get the data paths(both src and local directory paths), and create DataIngestionConfig object. Present in ```src/{project_name}/config/configuration.py```

```bash
(ROOT)
└── 🚀 Data Ingestion Pipeline Workflow

    ├── 1️⃣ TRIGGER (How it starts)
    │   └── DVC Command: `dvc repro`
    │       └── Reads `dvc.yaml` to find the 'data_ingestion' stage.
    │
    ├── 2️⃣ ORCHESTRATION (The Conductor)
    │   ├── 📜 dvc.yaml
    │   │   └── Defines the stage & executes the command:
    │   │       └── `python src/cnnClassifier/pipeline/stage_01_data_ingestion.py`
    │   │
    │   └── 🐍 stage_01_data_ingestion.py
    │       ├── Purpose: Manages the execution flow for this specific stage.
    │       ├── Step 1: Initializes the ConfigurationManager.
    │       └── Step 2: Calls the Primary Code (DataIngestion component).
    │
    ├── 3️⃣ SECONDARY CODE (Configuration & Blueprint)
    │   ├── 📝 config/config.yaml (The Parameters)
    │   │   ├── Role: Stores all variables and paths.
    │   │   └── Contains: `source_URL`, `unzip_dir`, etc.
    │   │
    │   ├── 🧱 src/cnnClassifier/entity/config_entity.py (The Schema)
    │   │   ├── Role: Defines the structure of the configuration.
    │   │   └── Contains: `DataIngestionConfig` dataclass.
    │   │
    │   └── 🌉 src/cnnClassifier/config/configuration.py (The Bridge)
    │       ├── Role: Reads the YAML, validates it, and creates a structured Python object.
    │       └── Method: `get_data_ingestion_config()` returns a `DataIngestionConfig` object.
    │
    ├── 4️⃣ PRIMARY CODE (The Engine / The "Doer")
    │   └── ⚙️ src/cnnClassifier/components/data_ingestion.py
    │       ├── Class: `DataIngestion`
    │       ├── Receives: The `DataIngestionConfig` object from the orchestrator.
    │       ├── Action 1: `download_file()`
    │       │   └── Uses `urllib` to download `data.zip` from the `source_URL`.
    │       └── Action 2: `extract_zip_file()`
    │           └── Uses `zipfile` to unzip `data.zip` into the `unzip_dir`.
    │
    └── 5️⃣ OUTPUT (The Result)
        └── 📂 artifacts/data_ingestion/
            ├── 📄 data.zip (The downloaded file)
            └── 🖼️ Chicken-fecal-images/... (The extracted image folders)

```








## Workflows

1. Update config.yaml               ‾‾‾‾‾‾‾|
2. Update secrets.yaml [Optional]          |(Update files outside src first, except dvc.yaml)
3. Update params.yaml               _______|
4. Update the entity
5. Update the configuration manager in src config(src/project_name/config/configuration.py)
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml



### Note:
* In Python, any directory that contains an __init__.py file is considered a package.
* Within a package, individual Python files (.py files) are considered modules.
* logs folder is not created using template.py


Given/shared a dataset
1) Download the dataset zip/Url -> define your dataset paths and their datatypes (config/config.yaml)
2) Paths/parameters saved in config.yaml should be read and initialised(src/project_name/constants/__init__.py)