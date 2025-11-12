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

### Note:
* logs folder is not created using template.py