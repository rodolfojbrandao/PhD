# otimizacao RL HC OX
import numpy as np
import scipy.optimize

a = np.linspace(-1.41,1.41,99)
x1 = 0
x2 = 0
x3 = 0
#obj1
z=0.3   #rl
b=0.5   #hc
c=0.2   #nt
#obj2
d=0.6   #rl
e=0.4   #ox
#obj3
m=0.3   #rl
n=0.3   #hc
o=0.2   #nt
p=0.2   #ox

rl=0
hc=0
ox=0
nt=0

RL_maxi = 30.30-4.46*x1+3.41*x1**2+4.02*x2**2-3.26*x3-5.52*x3**2+8.01*x1*x2+2.28*x1*x3+1.65*x2*x3
RL_mini = 30.30-4.46*x1+3.41*x1**2+4.02*x2**2-3.26*x3-5.52*x3**2+8.01*x1*x2+2.28*x1*x3+1.65*x2*x3
HC_maxi = 13.71-2.09*x2-1.9*x2**2+3.38*x3**2-3.46*x2*x3
HC_mini = 13.71-2.09*x2-1.9*x2**2+3.38*x3**2-3.46*x2*x3
OX_maxi = 38.88-3.82*x1-5.82*x2-7.07*x2**2+5.86*x3**2+5.39*x1*x2+6.17*x1*x3
OX_mini = 38.88-3.82*x1-5.82*x2-7.07*x2**2+5.86*x3**2+5.39*x1*x2+6.17*x1*x3
NT_maxi = 27.12 + 5.51*x1**2+3.56*x2+5.52*x2**2-6.47*x3**2+7.47*x2*x3
NT_mini = 27.12 + 5.51*x1**2+3.56*x2+5.52*x2**2-6.47*x3**2+7.47*x2*x3
f_OBJ1=z*rl/RL_maxi+b*hc/HC_maxi-c*nt/NT_maxi
f_OBJ2=d*rl/RL_maxi-e*ox/OX_maxi
f_OBJ3=m*rl/RL_maxi+n*hc/HC_maxi-o*nt/NT_maxi-p*ox/OX_maxi

for i in range(0, len(a)):
    x1 = a[i]
    for j in range(0, len(a)):
        x2 = a[j]
        for k in range(0, len(a)):
            x3 = a[k]
            rl = 30.30-4.46*x1+3.41*x1**2+4.02*x2**2-3.26*x3-5.52*x3**2+8.01*x1*x2+2.28*x1*x3+1.65*x2*x3
            hc = 13.71-2.09*x2-1.9*x2**2+3.38*x3**2-3.46*x2*x3
            ox = 38.88-3.82*x1-5.82*x2-7.07*x2**2+5.86*x3**2+5.39*x1*x2+6.17*x1*x3
            nt = 27.12+5.51*x1**2+3.56*x2+5.52*x2**2-6.47*x3**2+7.47*x2*x3
            if rl>RL_maxi:
                RL_maxi = rl.copy()
                x1_maxi_RL = x1
                x2_maxi_RL = x2
                x3_maxi_RL = x3
            elif rl<RL_mini:
                RL_mini = rl.copy()
                x1_mini_RL = x1
                x2_mini_RL = x2
                x3_mini_RL = x3
            if hc > HC_maxi:
                HC_maxi = hc.copy()
                x1_maxi_HC = x1
                x2_maxi_HC = x2
                x3_maxi_HC = x3
            elif hc < HC_mini:
                HC_mini = hc.copy()
                x1_mini_HC = x1
                x2_mini_HC = x2
                x3_mini_HC = x3
            if ox > OX_maxi:
                OX_maxi = ox.copy()
                x1_maxi_OX = x1
                x2_maxi_OX = x2
                x3_maxi_OX = x3
            elif ox < OX_mini:
                OX_mini = ox.copy()
                x1_mini_OX = x1
                x2_mini_OX = x2
                x3_mini_OX = x3
            if nt > NT_maxi:
                NT_maxi = nt.copy()
                x1_maxi_NT = x1
                x2_maxi_NT = x2
                x3_maxi_NT = x3
            elif nt < NT_mini:
                NT_mini = nt.copy()
                x1_mini_NT = x1
                x2_mini_NT = x2
                x3_mini_NT = x3
RL_maxi = 57
print(f' maximo de RL eh de {RL_maxi:.2f} com x1 de {x1_maxi_RL:.2f}, x2 de {x2_maxi_RL:.2f} e x3 de {x3_maxi_RL:.2f}')
print(f' minimo de RL eh de {RL_mini:.2f} com x1 de {x1_mini_RL:.2f}, x2 de {x2_mini_RL:.2f} e x3 de {x3_mini_RL:.2f}')

print(f' maximo de HC eh de {HC_maxi:.2f} com x1 de {x1_maxi_HC:.2f}, x2 de {x2_maxi_HC:.2f} e x3 de {x3_maxi_HC:.2f}')
print(f' minimo de HC eh de {HC_mini:.2f} com x1 de {x1_mini_HC:.2f}, x2 de {x2_mini_HC:.2f} e x3 de {x3_mini_HC:.2f}')

print(f' maximo de OX eh de {OX_maxi:.2f} com x1 de {x1_maxi_OX:.2f}, x2 de {x2_maxi_OX:.2f} e x3 de {x3_maxi_OX:.2f}')
print(f' minimo de OX eh de {OX_mini:.2f} com x1 de {x1_mini_OX:.2f}, x2 de {x2_mini_OX:.2f} e x3 de {x3_mini_OX:.2f}')

print(f' maximo de NT eh de {NT_maxi:.2f} com x1 de {x1_maxi_NT:.2f}, x2 de {x2_maxi_NT:.2f} e x3 de {x3_maxi_NT:.2f}')
print(f' minimo de NT eh de {NT_mini:.2f} com x1 de {x1_mini_NT:.2f}, x2 de {x2_mini_NT:.2f} e x3 de {x3_mini_NT:.2f}')



for i in range(0, len(a)):
    x1 = a[i]
    for j in range(0, len(a)):
        x2 = a[j]
        for k in range(0, len(a)):
            x3 = a[k]
            rl = 30.30-4.46*x1+3.41*x1**2+4.02*x2**2-3.26*x3-5.52*x3**2+8.01*x1*x2+2.28*x1*x3+1.65*x2*x3
            hc = 13.71-2.09*x2-1.9*x2**2+3.38*x3**2-3.46*x2*x3
            ox = 38.88-3.82*x1-5.82*x2-7.07*x2**2+5.86*x3**2+5.39*x1*x2+6.17*x1*x3
            nt = 27.12+5.51*x1**2+3.56*x2+5.52*x2**2-6.47*x3**2+7.47*x2*x3
            f_obj1=z*rl/RL_maxi+b*hc/HC_maxi-c*nt/NT_maxi
            f_obj2=d*rl/RL_maxi-e*ox/OX_maxi
            f_obj3=m*rl/RL_maxi+n*hc/HC_maxi-o*nt/NT_maxi-p*ox/OX_maxi
            if f_obj1 > f_OBJ1:
                f_OBJ1 = f_obj1.copy()
                x1_OBJ1 = x1
                x2_OBJ1 = x2
                x3_OBJ1 = x3
                rl_OBJ1=rl
                hc_OBJ1=hc
                nt_OBJ1=nt
            if f_obj2 > f_OBJ2:
                f_OBJ2 = f_obj2.copy()
                x1_OBJ2 = x1
                x2_OBJ2 = x2
                x3_OBJ2 = x3
                rl_OBJ2 = rl
                ox_OBJ2 = ox
            if f_obj3 > f_OBJ3:
                f_OBJ3 = f_obj3.copy()
                x1_OBJ3 = x1
                x2_OBJ3 = x2
                x3_OBJ3 = x3
                rl_OBJ3 = rl
                hc_OBJ3 = hc
                nt_OBJ3 = nt
                ox_OBJ3 = ox
print('=============================================================================================')
print(f' obj1 com valor de {f_OBJ1:.2f} com x1 de {x1_OBJ1:.2f}, x2 de {x2_OBJ1:.2f} e x3 de {x3_OBJ1:.2f}')
print(f' rl com valor de {rl_OBJ1:.2f} com hc de {hc_OBJ1:.2f}, e nt de {nt_OBJ1:.2f}')
print('=============================================================================================')
print(f' obj2 com valor de {f_OBJ2:.2f} com x1 de {x1_OBJ2:.2f}, x2 de {x2_OBJ2:.2f} e x3 de {x3_OBJ2:.2f}')
print(f' rl com valor de {rl_OBJ2:.2f} com ox de {ox_OBJ2:.2f}')
print('=============================================================================================')
print(f' obj3 com valor de {f_OBJ3:.2f} com x1 de {x1_OBJ3:.2f}, x2 de {x2_OBJ3:.2f} e x3 de {x3_OBJ3:.2f}')
print(f' rl com valor de {rl_OBJ3:.2f} hc de {hc_OBJ3:.2f} nt de {nt_OBJ3:.2f} com ox de {ox_OBJ3:.2f}')