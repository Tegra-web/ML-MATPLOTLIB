import os
import sys

dossierBase = os.path.dirname(__file__)

sys.path.append(dossierBase)

from traitement_data import data 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 

#Diviser en parametre les entrées et la sortie
x = data.iloc[:, :-1]
y = data.iloc[:,-1]

# diviser les données de test et d'entrai

x_train,x_test,y_train,y_test = train_test_split(x,y, test_size = 0.75,random_state=40)

scal = StandardScaler()
x_train = scal.fit_transform(x_train)
x_test = scal.transform(x_test)




if __name__ == "__main__":
    print(x_train.shape)
