import pandas as pd

dossier = pd.read_csv("Maldie_du_coeur/datasets/raw_data/heart_disease.csv", header=None)

print(dossier.describe())
print(dossier.shape)
print(dossier.columns)


print("Aperçu des données :")
print(dossier.head())

print("\nInfos générales :")
print(dossier.info())

print("\nValeurs manquantes :")
print(dossier.isnull().sum())
