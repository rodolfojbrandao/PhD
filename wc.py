import os
import numpy as np
import pandas as pd
import math
from pandas import DataFrame

NF = 350 #number of files
NP = 16311 #number of particles

vX = np.zeros((NP,NF))
vY = np.zeros((NP,NF))
vZ = np.zeros((NP,NF))

path='/media/rodolfo/5A0819190818F5AB/Doutorado/numerico/regimes/ValidacaoExperimental/37/dados'
os.chdir(path)

for j in range (220,NF):
    Dados = pd.read_csv('dados.{}.csv'.format(j))
    concluido=j/NF*100
    print(concluido)
    print(j)
    vX[:, j] = Dados.iloc[:, 2].copy()
    vY[:, j] = Dados.iloc[:, 3].copy()
    vZ[:, j] = Dados.iloc[:, 4].copy()

vX=pd.DataFrame(vX)
vY=pd.DataFrame(vY)
vZ=pd.DataFrame(vZ)

v=np.sqrt(np.square(vX)+np.square(vY)+np.square(vZ))

V=v.mean(axis = 0)
V.to_csv('Velocidade37.csv')