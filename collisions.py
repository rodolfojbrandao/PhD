import os
import numpy as np
import pandas as pd
import math
from pandas import DataFrame

NF = 601 #number of files
NP = 71 #number of particles
collisions = pd.DataFrame(np.zeros((NP,NF)))
col = pd.DataFrame(np.zeros((NF,1)))
path='/home/rodolfo/Desktop/raphael/CSVs'
os.chdir(path)

for j in range (0,NF):
    filenumber=50000+1000*j
    Dados = pd.read_csv('dump{}.csv'.format(filenumber))
    collisions=pd.DataFrame(Dados)
    collisions.drop(collisions.index[0:8], inplace=True)
    collisions.sum(axis=1, skipna=True)
    col.iloc[j,0]=collisions.values.sum()
totalcollisions=col.sum().sum()

print(collisions)
print(filenumber)
print(col)
print(totalcollisions)