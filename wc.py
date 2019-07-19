import os
import numpy as np
import pandas as pd
import math
from pandas import DataFrame

NF = 800 #number of files
NP = 33215 #number of particles

posicaoX = np.zeros((NP,NF))
posicaoY = np.zeros((NP,NF))
posicaoZ = np.zeros((NP,NF))
vX = np.zeros((NP,NF))
vY = np.zeros((NP,NF))
vZ = np.zeros((NP,NF))

path='/home/rodolfo/Desktop/02/dados'
os.chdir(path)

for j in range (0,NF):
    Dados = pd.read_csv('dados.{}.csv'.format(j))
    posicaoX[:, j] = Dados.iloc[:, 6].copy()
    posicaoY[:, j] = Dados.iloc[:, 7].copy()
    posicaoZ[:, j] = Dados.iloc[:, 8].copy()
    vX[:, j] = Dados.iloc[:, 2].copy()
    vY[:, j] = Dados.iloc[:, 3].copy()
    vZ[:, j] = Dados.iloc[:, 4].copy()

vX=pd.DataFrame(vX)
vY=pd.DataFrame(vY)
vZ=pd.DataFrame(vZ)
posicaoX=pd.DataFrame(posicaoX)
posicaoY=pd.DataFrame(posicaoY)
posicaoZ=pd.DataFrame(posicaoZ)

v=np.square(vX)+np.square(vY)+np.square(vZ)

max_x = float(posicaoX.iloc[:,[1]].max())
max_y = float(posicaoY.iloc[:,[1]].max())
max_z = float(posicaoZ.iloc[:,[1]].max())
min_x = float(posicaoX.iloc[:,[1]].min())
min_y = float(posicaoY.iloc[:,[1]].min())
min_z = float(posicaoZ.iloc[:,[1]].min())

V=v.mean(axis = 0)
V.to_csv('Velocidade.csv')