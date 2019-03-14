# otimizacao RL HC OX
import numpy as np

a = [20, 25, 30, 35, 40]
b = [2, 4, 6, 8, 10, 12]
c = [10, 20, 30, 40, 50]

x1 = 0
x2 = 0
x3 = 0

y1=0
y2=0
d1=0
d2=0
d=0
D=0

y1_maxi = 1662.78+107.95*x1-78.82*x2+23.12*x3-2.29*x1*x1+21.72*x2*x2-0.572*x3*x3-6.34*x1*x2+1.516*x1*x3-3.758*x2*x3
y1_mini = 1662.78+107.95*x1-78.82*x2+23.12*x3-2.29*x1*x1+21.72*x2*x2-0.572*x3*x3-6.34*x1*x2+1.516*x1*x3-3.758*x2*x3
y2_maxi = 14.185-0.392*x1+0.446*x2-0.111*x3+0.006*x1*x1+0.023*x2*x2-0.0014*x3*x3+0.009*x1*x2+0.002*x1*x3+0.004*x2*x3
y2_mini = 14.185-0.392*x1+0.446*x2-0.111*x3+0.006*x1*x1+0.023*x2*x2-0.0014*x3*x3+0.009*x1*x2+0.002*x1*x3+0.004*x2*x3

x1_maxi_y1 = 20
x2_maxi_y1 = 2
x3_maxi_y1 = 10
x1_mini_y1 = 20
x2_mini_y1 = 2
x3_mini_y1 = 10
x1_maxi_y2 = 20
x2_maxi_y2 = 2
x3_maxi_y2 = 10
x1_mini_y2 = 20
x2_mini_y2 = 2
x3_mini_y2 = 10

for i in range(0, len(a)):
    x1 = a[i]
    for j in range(0, len(b)):
        x2 = b[j]
        for k in range(0, len(c)):
            x3 = c[k]
            y1 = 1662.78+107.95*x1-78.82*x2+23.12*x3-2.29*x1*x1+21.72*x2*x2-0.572*x3*x3-6.34*x1*x2+1.516*x1*x3-3.758*x2*x3
            y2 = 14.185-0.392*x1+0.446*x2-0.111*x3+0.006*x1*x1+0.023*x2*x2-0.0014*x3*x3+0.009*x1*x2+0.002*x1*x3+0.004*x2*x3
            if y1>y1_maxi:
                y1_maxi = y1
                x1_maxi_y1 = x1
                x2_maxi_y1 = x2
                x3_maxi_y1 = x3
            elif y1<y1_mini:
                y1_mini = y1
                x1_mini_y1 = x1
                x2_mini_y1 = x2
                x3_mini_y1 = x3
            if y2 > y2_maxi:
                y2_maxi = y2
                x1_maxi_y2 = x1
                x2_maxi_y2 = x2
                x3_maxi_y2 = x3
            elif y2 < y2_mini:
                y2_mini = y2
                x1_mini_y2 = x1
                x2_mini_y2 = x2
                x3_mini_y2 = x3

print('=============================================================================================')
print(' maximo de y1 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y1_maxi,x1_maxi_y1,x2_maxi_y1,x3_maxi_y1))
print(' minimo de y1 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y1_mini,x1_mini_y1,x2_mini_y1,x3_mini_y1))
print('=============================================================================================')

print(' maximo de y2 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y2_maxi,x1_maxi_y2,x2_maxi_y2,x3_maxi_y2))
print(' minimo de y2 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y2_mini,x1_mini_y2,x2_mini_y2,x3_mini_y2))

for i in range(0, len(a)):
    x1 = a[i]
    for j in range(0, len(b)):
        x2 = b[j]
        for k in range(0, len(c)):
            x3 = c[k]
            y1 = 1662.78+107.95*x1-78.82*x2+23.12*x3-2.29*x1*x1+21.72*x2*x2-0.572*x3*x3-6.34*x1*x2+1.516*x1*x3-3.758*x2*x3
            y2 = 14.185-0.392*x1+0.446*x2-0.111*x3+0.006*x1*x1+0.023*x2*x2-0.0014*x3*x3+0.009*x1*x2+0.002*x1*x3+0.004*x2*x3
            d1=(y1-y1_mini)/(y1_maxi-y1_mini)
            d2=(y2-y2_mini)/(y2_maxi-y2_mini)
            d=d1*d2

            if d > D:
                D = d
                x1_opt = x1
                x2_opt = x2
                x3_opt = x3
                y1_opt=y1
                y2_opt=y2

print('=============================================================================================')
print(' ponto otimo com valor de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(D,x1_opt,x2_opt,x3_opt))
print(' y1 com valor de {:.2f} com y2 de {:.2f}'.format(y1_opt,y2_opt))
