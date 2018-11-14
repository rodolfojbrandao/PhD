import os
import numpy as np
import pandas as pd
from multiprocessing import Pool
import math

path='/media/rodolfo/5A0819190818F5AB/DOUTORADO-SIMULACOES-COMPLETAS/Difusividade-granular/05/dados'
os.chdir(path)

NF = 49 #number of files
NP = 25000 #number of particles
ts = 1

posicaoX = np.zeros((5,NF))
posicaoY = np.zeros((5,NF))
posicaoZ = np.zeros((5,NF))
deltaX = np.zeros((5,NF))
deltaY = np.zeros((5,NF))
deltaZ = np.zeros((5,NF))
distancia = np.zeros((5,NF))
Deff = np.zeros((5,NF))
Deff_X = np.zeros((5,NF))
Deff_Y = np.zeros((5,NF))
Deff_Z = np.zeros((5,NF))

for j in range (0,NF):
    Dados = pd.read_csv('dados.{}.csv'.format(j))
    for i in range (0,NP):
        if Dados.iloc[i, 0] == 1:
            posicaoX[0, j] = Dados.iloc[i, 6].copy()
            posicaoY[0, j] = Dados.iloc[i, 7].copy()
            posicaoZ[0, j] = Dados.iloc[i, 8].copy()
        if Dados.iloc[i, 0] == 2:
            posicaoX[1, j] = Dados.iloc[i, 6].copy()
            posicaoY[1, j] = Dados.iloc[i, 7].copy()
            posicaoZ[1, j] = Dados.iloc[i, 8].copy()
        if Dados.iloc[i, 0] == 3:
            posicaoX[2, j] = Dados.iloc[i, 6].copy()
            posicaoY[2, j] = Dados.iloc[i, 7].copy()
            posicaoZ[2, j] = Dados.iloc[i, 8].copy()
        if Dados.iloc[i, 0] == 4:
            posicaoX[3, j] = Dados.iloc[i, 6].copy()
            posicaoY[3, j] = Dados.iloc[i, 7].copy()
            posicaoZ[3, j] = Dados.iloc[i, 8].copy()
        if Dados.iloc[i, 0] == 5:
            posicaoX[4, j] = Dados.iloc[i, 6].copy()
            posicaoY[4, j] = Dados.iloc[i, 7].copy()
            posicaoZ[4, j] = Dados.iloc[i, 8].copy()

posicaoX = pd.DataFrame(posicaoX)
posicaoY = pd.DataFrame(posicaoY)
posicaoZ = pd.DataFrame(posicaoZ)

#print(posicaoX)
for m in range (0,NF-1):
    for n in range (0,5):
        deltaX[n,m] = abs(posicaoX.iloc[n,m+1]-posicaoX.iloc[n,m])
        deltaY[n,m] = abs(posicaoY.iloc[n,m+1]-posicaoY.iloc[n,m])
        deltaZ[n,m] = abs(posicaoZ.iloc[n,m+1]-posicaoZ.iloc[n,m])
        distancia[n,m] =  math.sqrt(deltaX[n,m]*deltaX[n,m]+deltaY[n,m]*deltaY[n,m]+deltaZ[n,m]*deltaZ[n,m])
        Deff[n,m] = distancia[n,m]*distancia[n,m]/ts
        Deff_X[n,m] = deltaX[n,m]*deltaX[n,m]/ts
        Deff_Y[n,m] = deltaY[n,m]*deltaY[n,m]/ts
        Deff_Z[n,m] = deltaZ[n,m]*deltaZ[n,m]/ts


deltaX = pd.DataFrame(deltaX)
Deff_X = pd.DataFrame(Deff_X)
Deff_Y = pd.DataFrame(Deff_Y)
Deff_Z = pd.DataFrame(Deff_Z)

distancia = pd.DataFrame(distancia)
Deff = pd.DataFrame(Deff)
#Deff.to_csv('Deff.csv')

#print(deltaX)
#print('==========distancia=================')
#print(distancia)
#print('==========Deff=================')
#print(Deff)

Deff_medio=Deff.mean(axis=1).mean()
Deff_X_medio=Deff_X.mean(axis=1).mean()
Deff_Y_medio=Deff_Y.mean(axis=1).mean()
Deff_Z_medio=Deff_Z.mean(axis=1).mean()

#print(Deff_medio)
print(Deff_X_medio)
print(Deff_Y_medio)
print(Deff_Z_medio)

Difusividade_radial=(Deff_X_medio+Deff_Y_medio)/2
#print('=======================================')
#print('Difusividade radial:',Difusividade_radial)
#print('=======================================')
#print('Difusividade axial:',Deff_Z_medio)


