import os
import pandas as pd

dossier_actuel = os.path.dirname((__file__))
liason = os.path.join(dossier_actuel,'heart_disease.csv')

data = pd.read_csv(liason)

if __name__ == "__main__":

    print(data.head())