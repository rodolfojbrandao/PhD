import os
import numpy as np
import pandas as pd
from multiprocessing import Pool

N = 8 #number of cores
a = list(range(N))
NF = 500
path='/home/hp/Desktop/dados'
os.chdir(path)

def f(a):
    inicio = int(a*NF/N)
    fim = int((a+1)*NF/N)
    for j in range(inicio,fim):
            data = pd.read_csv(f'dados.{j}.csv')
            data = data.drop(['id', 'f:0', 'f:1', 'f:2', 'omega:0', 'omega:1', 'omega:2'], axis = 1)
            data.to_csv(f'dados.{j}.csv')

if __name__=='__main__':
    Tarefas=len(a)
    with Pool(Tarefas) as p:
        p.map(f,a)