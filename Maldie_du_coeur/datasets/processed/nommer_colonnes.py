import pandas as pd

import os 
import sys


dir_base = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir_base)

from raw_data.import_brut import data


colonnes = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",  
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
    "target"
]

data.columns = colonnes

if __name__ == "__main__": 
    print(data.info())
    print(data.head())