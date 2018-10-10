import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from multiprocessing import Pool
import statsmodels.api as sm
import statsmodels.formula.api as smf # pacotes estatisticos

path='/home/rodolfo//Dropbox/Doutorado/Resultados/segregacao-efeito-combinado-tamanho-densidade'

os.chdir(path)
# dados disponiveis: 03 04 07 11 12 13 14 15 16 18 19 20 22 23 24 25
i=0
j=3

Dados = pd.read_csv('dados{}{}.csv'.format(i,j))

print(Dados)
#os dados de segregacao nao estao normalizados
x = Dados.iloc[0:490,0]
y = Dados.iloc[0:490,4]
print(Dados.head())
plt.plot(x,y)
plt.ylabel('time (s)')
plt.xlabel('M ( - )')
plt.title('Dados {}{}'.format(i,j))
plt.show()
#formula1='MG ~ SL+time+TC+I(SL**2.0)+I(time**2.0)+I(TC**2.0)+I(TC*time)+I(TC*SL)+I(SL*time)' # MG em função das variaveis SL, time, TC
#est = smf.ols(formula1, data=DAT).fit()
#print(est.summary())