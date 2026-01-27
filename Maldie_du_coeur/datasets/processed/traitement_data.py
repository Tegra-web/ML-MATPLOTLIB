import os 
import sys
import pandas as pd
import numpy as np

dir_base = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir_base)

from processed.nommer_colonnes import colonnes
from raw_data.import_brut import data

#pour reduire a int32

data['target'] = data['target'].astype('int32')

# print(data['target'].dtype)

#visualiser les donnees manquantes

data = data.replace('?', np.nan)
data = data.astype(np.float32)
data = data.fillna(data.median())


# print("\nValeurs manquantes :")
# print(data.isna().sum())

# #mapping 
# ca = {
#     '3' : 3,
#     '2' : 2,
#     '0' : 0,
#     '1' : 1
# }

# thal = {
#     '3' : 3,
#     '7' : 7,
#     '6' : 6
# }
# print (data['ca'].unique())

# print (data['thal'].unique())

# data['dic_ca'] = data['ca'].map(ca)
# data['ca'] = data['ca'].astype('int32')

# data['dic_thal'] = data['thal'].map(thal)
# data['thal'] = data['thal'].astype('int32')


# print(data['ca'].dtype)
# print(data['thal'].dtype)

if __name__ == "__main__":
    print(data.info())








