import os
import numpy as np
import pandas as pd
import math
from pandas import DataFrame

NF = 601 #number of files
NP = 71 #number of particles

collisions = np.zeros((NP,NF))
col = pd.DataFrame(np.zeros((NF,1)))
path='/home/rodolfo/Desktop/raphael/CSVs'
os.chdir(path)

for j in range (0,NF):
    filenumber=50000+1000*j
    Dados = pd.read_csv('dump{}.csv'.format(filenumber))
    collisions[:, j] = Dados.iloc[:, 1].copy()
    col=np.sum(collisions, axis=0)
    col = pd.DataFrame(col)
col.to_csv('dados.csv')
