#programa para dimensionamento de um torcador de calor tubo duplo
#considerações: contra corrente
#               o diâmetro será determinado pelos diâmetros comercialmente disponíveis
#               fluido a ser aquecido passa no tubo interno

#importação de biblioteca numérica
import numpy as np
from scipy.optimize import fsolve


#propriedades do tubo e do fluido
print("Material: Cobre")
k1=292.41/(100*3600)#condutividade térmica do COBRE k=[kcal/(h*m*°c)]*[1m/100cm]*[1h/3600s]
K2= 0 #condutividade térmica do ALUMINIO k[kcal/(h*m*°c)] atenção as unidades
K=k1

#diâmetros e espessuras comerciais
#minúsculas dizem respeito ao tubo interno e maiúsculo ao tubo externo

#tubo interno
do=np.array([15,22,28,35,42,54])/10 #Do[cm]
esp=np.array([0.5,0.6,0.6,0.7,0.8,0.9])/10
print(f"diâmetros internos do tubo interno: {do-esp}")

#tubo externo
#considerando diâmetrod do catálogo da trige
Do=np.array([32, 40, 50, 60])/10 #cm
espe=np.array([2.1, 2.4, 3.0, 3.3])/10 #cm
Di=Do-espe
print(f"Diâmetros internos do tubo externo: {Di} cm")

#propriedades do fluido
Cp = 1         #Cp=[cal/g.°C]
mi = 0.006531 #mi=[Po]
rho = 1        #roh=[g/cm3] a 40°C
pr=mi*Cp/K

#Tempera[°C] dos fluidos
Tqe=60
Tfe=28
Tfs=43

w=0
#laços de cálculo
for i in Di: # i representa "Di" da rodada
    w = w +1
    Ri = i / 2
    qq = 2 #vazões volumétricas
    mq = qq*1000 #mássicas são iguais ( m = q(l/min) * roh(g/cm3)* (1000cm3/1L); roh=1g/cm3)
    while 0.5 < qq: #repetição para vazões de corrente quente | tubo externo
        qq = qq - 0.1
        qf = 0.5
        mf = qf*1000
        while qf < 2: #repetição para vazões de corrente fria | tubo interno
            Q = mf*Cp*(Tfs-Tfe)/60 # Q=[(g/min)*(cal/g*°C)*(°C)]*[1m/60s]
            Tqs = Tqe-((mf/mq)*(Tfs-Tfe))
            z = 0
            qf = qf + 0.1
            for n in do:
                ro = n/2
                di = n-esp[z]
                z = z + 1
                ri = di/2
                #print(f"volta: {w}.{z}\n ")
                if ri < Ri:
                    #print(f"ri < Ri\n ri={ri} cm e Ri={Ri} cm\n")
                    V = (qq+0.1)/(np.pi*(Ri ** 2 - ri ** 2))  # velocidade no tubo externo
                    v = (qf - 0.1)/(np.pi*(ri**2))
                    De = (i**2 - n**2)/n
                    #print(f"De={De} cm \n\n")
                    re = (rho*n*v)/mi  # reynolds para escoamento no tubo interno
                    Re = (rho*De*V)/mi  # reynolds para escoamento no tubo externo
                    DT1 = Tqe - Tfs
                    DT2 = Tqs - Tfe
                    DTf = Tqe - Tqs
                    DTq = Tfs - Tfe
                    #print(f"Tfe = {Tfe} \nTfs ={Tfs}\nDTf = {DTf}\n")
                    #print(f"Tqe = {Tqe} \nTqs ={Tqs}\nDTq = {DTq}\n")
                    if DT1!=0 or DT2!=0 or (np.log(DT1/DT2))!=0:
                        DTm = ((DT1)-(DT2))/np.log((DT1)/(DT2))
                    if re > 2100 and Re > 2100:
                        nu = 0.023*(re**0.8)*(pr**0.4)
                        hi = nu*K/n  # hi=[kcal/(s*cm*°C)]
                        Nu = 0.023*(Re**0.8)*(pr ** 0.3)
                        ho = Nu*K/De  # ho=[kcal/(s*cm*°C)]*
                    if Re < 2100 and re < 2100:
                        def laminar(L):  # para o tubo interno
                            l = L[0]
                            hi = L[1]
                            ho = L[2]
                            U = L[3]

                            F = np.empty((4))
                            F[0] = hi * n / K - 1.86 * (re * pr * n / l) ** (1 / 3)
                            F[1] = ho * De / K - 1.86 * (Re * pr * De / l) ** (1 / 3)
                            F[2] = U - 1 / ((ro / (hi * ri)) + (1 / ho) + (ro * np.log(ro / ri) / (K)))  # U=[kcal/(s*cm*°C)]]
                            F[3] = Q - U * 2 * np.pi * l * DTm
                            return F
                        LGuess = np.array([0.5,1,1,0.1])
                        L = fsolve(laminar,LGuess)
                    else:
                        U=1/((ro/(hi*ri))+(1/ho)+(ro*np.log(ro/ri)/(K)))  # U=[kcal/(s*cm*°C)]]
                        L = Q / (2 * np.pi * ro * DTm)
                    if L[0] < 100 and L[0] >= 60:
                        print(f"Vazão da corrente fria: {qf - 0.1}")
                        print(f"Vazão da corrente quente: {qq + 0.1}")
                        print(f"Temperatura de saída da corrente quente: {Tqs} °C")
                        #print(f"diâmetro do tubo externo sendo utilizado: {i}cm")
                        #print(f"diâmetro do tubo interno sendo utilizado: {di}cm")
                        #print(f"reynolds no tubo interno: {re}\n"
                        #      f"reynolds no tubo externo: {Re}")
                        #print(f"Q = {Q} \nhi = {L[1]} \nho = {L[2]} \nU = {L[3]}")
                        print(f"\ncomprimento válido:{L[0]/100} m\n\n\n\n")


