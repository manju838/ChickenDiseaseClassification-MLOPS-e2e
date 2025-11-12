# ChickenDiseaseClassification-MLOPS-e2e
Follows https://www.youtube.com/watch?v=p1bfK8ZJgkE

# Steps

```bash
$conda create -n chicken python=3.10 pip
$conda activate chicken

#Make sure:
$which pip
/c/Users/manju/.conda/envs/chicken/Scripts/pip
# Failing this means pip is not using/pointed to isolated env completely and can cause package version conflict issues with random packages in your laptop.

$pip install -r requirements.txt
```

# Note:
* Logging is added in the project_name's constructor file(src/template_project_name) so that it automatically gets imported 