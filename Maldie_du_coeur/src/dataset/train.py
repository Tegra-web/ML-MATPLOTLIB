import os 
import sys

dir_base = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(dir_base)
from datasets.processed.splitdata import x_train, y_train 

