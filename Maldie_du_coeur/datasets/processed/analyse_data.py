import os 
import sys


dir_base = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir_base)

from raw_data.import_brut import data

if __name__ == "__main__": 
    print(data.info())