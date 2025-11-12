"""
- In this repo, we create packages in src and execute them from here.
- So, all model components, data preprocessing, training code, postprocessing code will be in src/{project_or_packagename}. 
- setup.py file recognises src/{project_or_packagename} as a package(when we run pip install -e . or add -e . in requirements.txt) and we can import modules from there.
"""

from cnnClassifier import logger

logger.info("Testing cnnClassifier package's custom logging module")