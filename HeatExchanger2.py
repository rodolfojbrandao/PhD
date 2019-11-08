import numpy as np
from scipy.optimize import fsolve


#propriedades do tubo e do fluido
K=292.41/(100*3600)#condutividade térmica do COBRE k=[kcal/(h*m*°c)]*[1m/100cm]*[1h/3600s]

#diâmetros e espessuras comerciais
#minúsculas dizem respeito ao tubo interno e maiúsculo ao tubo externo

#tubo interno
do=np.array([15,22,28,35,42,54])/10 #Do[cm]
esp=np.array([0.5,0.6,0.6,0.7,0.8,0.9])/10

#tubo externo
#considerando diâmetrod do catálogo da trige
Do=np.array([32, 40, 50, 60])/10 #cm
espe=np.array([2.1, 2.4, 3.0, 3.3])/10 #cm
Di=Do-espe

ro=do/2
di = ro-esp
ri=di/2
Ri=Di/2

#propriedades do fluido
Cp = 1         #Cp=[cal/g.°C]
mi = 0.006531 #mi=[Po]
rho = 1        #roh=[g/cm3] a 40°C
pr=mi*Cp/K

#Tempera[°C] dos fluidos
Tqe=60
Tfe=28
Tfs=43

qq=np.arange(0.5,2.1,0.1)
mq=qq*1000
qf=np.arange(0.5,2.1,0.1)
mf=qf*1000
Q = mf*Cp*(Tfs-Tfe)/60 # Q=[(g/min)*(cal/g*°C)*(°C)]*[1m/60s]

#=================================================
Tqs=[]
for i in mf:
	for j in mq:
		Tqs.append(Tqe-((i/j)*(Tfs-Tfe))) 
#=================================================

#=================================================
De=[]
for i in di:
	for n in do:
		if i > n:			
			De.append((i**2 - n**2)/n)
#=================================================

#=================================================
V=[] # velocidade tudo externo
v=[] # velocidade tudo interno
#for i in qq:
#	for j in Ri
#=================================================