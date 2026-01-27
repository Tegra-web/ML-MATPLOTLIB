import os 
import sys
import torch

dossier_de_base = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dossier_de_base)
from dataset.train import x_train, y_train
from dataset.test import x_test, y_test
from model.mpl import MPL

x_train = torch.tensor(x_train, dtype=torch.float32)
y_train =  torch.tensor(y_train.values, dtype=torch.float32).view(-1,1)

x_test = torch.tensor(x_test, dtype=torch.float32)
y_test =  torch.tensor(y_test.values, dtype=torch.float32).view(-1,1)

