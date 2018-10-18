import os
import numpy as np
import pandas as pd
import math

#NF = 4 #number of files
NF = 8 #number of files
NP = 147465 #number of particles
raio1 = 0.0009
raio2 = 0.0021
rx = 5
ry = 5
rz = 10
tamanho = rx*ry*rz

velocidade_resultante = pd.DataFrame(np.zeros((NP,NF)))
contador1 = list()
contador2 = list()
contador = list()
np.linspace(0.1,49.0,NF)
posicaoX = np.zeros((NP,NF))
posicaoY = np.zeros((NP,NF))
posicaoZ = np.zeros((NP,NF))
Tipo = np.zeros((NP,NF))
Raio = np.zeros((NP,NF))
vx = np.zeros((NP,NF))
vy = np.zeros((NP,NF))
vz = np.zeros((NP,NF))
contador_tipo1 = np.zeros((tamanho,NF))
contador_tipo2 = np.zeros((tamanho,NF))
velocidade_tipo1 = np.zeros((tamanho,NF))
velocidade_tipo2 = np.zeros((tamanho,NF))
posicao_vetor = 1

path='/home/rodolfo/Desktop/dados'
os.chdir(path)

# leitura e separaçao de dados
for j in range (0,NF):
    Dados = pd.read_csv('dados.{}.csv'.format(j))
    posicaoX[:, j] = Dados.iloc[:, 6].copy()
    posicaoY[:,j] = Dados.iloc[:, 7].copy()
    posicaoZ[:,j] = Dados.iloc[:, 8].copy()
    Tipo[:,j] = Dados.iloc[:, 1].copy()
    Raio[:,j] = Dados.iloc[:, 5].copy()
    vx[:,j] = Dados.iloc[:, 2].copy()
    vy[:,j] = Dados.iloc[:, 3].copy()
    vz[:,j] = Dados.iloc[:, 4].copy()

posicaoX=pd.DataFrame(posicaoX)
posicaoY=pd.DataFrame(posicaoY)
posicaoZ=pd.DataFrame(posicaoZ)
Tipo=pd.DataFrame(Tipo)
Raio=pd.DataFrame(Raio)
vx=pd.DataFrame(vx)
vy=pd.DataFrame(vy)
vz=pd.DataFrame(vz)

gradeamentoX = (max(posicaoX) - min(posicaoX)) / rx
gradeamentoY = (max(posicaoY) - min(posicaoY)) / ry
gradeamentoZ = (max(posicaoZ) - min(posicaoZ)) / rz

for i in range(0,NF):
    velocidade_resultante.iloc[:,[i]] = vx.iloc[:,[i]]*vx.iloc[:,[i]]+vy.iloc[:,[i]]*vy.iloc[:,[i]]+vz.iloc[:,[i]]*vz.iloc[:,[i]]

velocidade_resultante=velocidade_resultante.pow(1./2)
V_medio = velocidade_resultante.mean(axis=0)

InferiorX=float(posicaoX.iloc[:,[1]].min())
InferiorY=float(posicaoY.iloc[:,[1]].min())
InferiorZ=float(posicaoZ.iloc[:,[1]].min())

for m in range(0,NF):
    p=0
    q=0
    for n in range(1, len(vx)):
        for pz in range(1,rz):
            for py in range(1,ry):
                for px in range(1,rx):
                    if posicaoX.iloc[[n],[m]]>InferiorX+(px-1)*gradeamentoX and posicaoX.iloc[[n],[m]]<InferiorX+px*gradeamentoX \
                        and posicaoY.iloc[[n],[m]]>InferiorY+(py-1)*gradeamentoY and posicaoY.iloc[[n],[m]]<InferiorY+py*gradeamentoY \
                            and posicaoZ.iloc[[n],[m]]>InferiorZ+(pz-1)*gradeamentoZ and posicaoZ.iloc[[n],[m]]<InferiorZ+pz*gradeamentoZ:
                        posicao_vetor = -30+px+5*py+25*pz