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
* 