import setuptools       # Facilitates the packaging and distribution of Python projects

# This setup.py file is executed when we do ```pip install -e .``` and recognises the SRC_REPO as a package. In this repo, we added ```-e .``` in requirements.txt so we dont need any other commands.

# Open Readme file as readmode
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Classification--Project"
AUTHOR_USER_NAME = "manju838" # Github username
SRC_REPO = "cnnClassifier" # Folder in src folder(project_name in template.py)
AUTHOR_EMAIL = "manjunadhkandavalli@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)