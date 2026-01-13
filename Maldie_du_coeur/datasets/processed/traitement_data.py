import os 
import sys
import pandas as pd
import numpy as np

dir_base = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir_base)

from processed.nommer_colonnes import colonnes
from raw_data.import_brut import data

"""pour reduire a int32"""

data['target'] = data['target'].astype('int32')

if __name__ == "__main__":
    print(data['target'].dtype)

#visualiser les donnees manquantes

data = data.replace('?', np.nan)
data = data.astype(np.float32)
data = data.fillna(data.median())


print("\nValeurs manquantes :")
print(data.isna().sum())

#mapping 
mapping_ca = {
    '3' : 3,
    '2' : 2,
    '0' : 0,
    '1' : 1
}

mapping_thal = {
    '3' : 3,
    '7' : 7,
    '6' : 6
}
print (data['ca'].unique())

print (data['thal'].unique())

data['ca'] = data['ca'].astype('float32')
data['thal'] = data['thal'].astype('float32')

print(data['ca'].dtype)
print(data['thal'].dtype)








