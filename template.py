"""
    Running this file creates a basic MLOPS template. 
"""
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",                   # workflows is directory for Github Actions worflows(CI/CD), .gitkeep forces git to track the empty folder
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",   # Contains individual, modular components of your machine learning pipeline
    f"src/{project_name}/utils/__init__.py",        # Contains generic utility functions and helper scripts, not belonging to single component
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",     # Defines the end-to-end machine learning pipelines by orchestrating the components
    f"src/{project_name}/entity/__init__.py",       # Define clear data structures, schemas, and return types for various components and stages in ML Pipeline
    f"src/{project_name}/constants/__init__.py",    # Stores constant values used throughout the project(env variables, filepaths, apikeys etc.)
    "config/config.yaml",                           # Main configuration file for the project
    "params.yaml",                                  # Parameters file for hyperparameters and other settings
    "dvc.yaml",                                     # Data Version Control(DVC) pipeline definition file
    "requirements.txt",
    "setup.py",                                     # Script for installing the "project_name" as a package
    "research/trials.ipynb",
    "templates/index.html"                          # HTML template for frontend interface  
]


for filepath in list_of_files:
    filepath = Path(filepath) # Converts linux style path to windows path
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")
