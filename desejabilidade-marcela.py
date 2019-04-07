# otimizacao RL HC OX
import numpy as np

a = [20,25,30,35,40]
b = [6, 9, 12]
c = [10, 30, 50]

x1 = 20
x2 = 6
x3 = 10

y1=0
y2=0
d1=0
d2=0
d=0
D=0

y1_maxi = 9803.455-382.115*x1-263.968*x2+1.917*x3+4.528*x1*x1+18.600*x2*x2-0.537*x3*x3-2.062*x1*x2+0.769*x1*x3+0.243*x2*x3
y1_mini = 9803.455-382.115*x1-263.968*x2+1.917*x3+4.528*x1*x1+18.600*x2*x2-0.537*x3*x3-2.062*x1*x2+0.769*x1*x3+0.243*x2*x3
y2_maxi = 8.655-2.581*x1-2.178*x2+12.716*x3+0.059*x1*x1+0.0496*x2*x2-0.074*x3*x3-0.021*x1*x2-0.0487*x1*x3+0.053*x2*x3
y2_mini = 8.655-2.581*x1-2.178*x2+12.716*x3+0.059*x1*x1+0.0496*x2*x2-0.074*x3*x3-0.021*x1*x2-0.0487*x1*x3+0.053*x2*x3

x1_maxi_y1 = 20
x2_maxi_y1 = 6
x3_maxi_y1 = 10
x1_mini_y1 = 20
x2_mini_y1 = 6
x3_mini_y1 = 10
x1_maxi_y2 = 20
x2_maxi_y2 = 6
x3_maxi_y2 = 10
x1_mini_y2 = 20
x2_mini_y2 = 6
x3_mini_y2 = 10

for i in range(0, len(a)):
    x1 = a[i]
    for j in range(0, len(b)):
        x2 = b[j]
        for k in range(0, len(c)):
            x3 = c[k]
            y1 = 9803.455-382.115*x1-263.968*x2+1.917*x3+4.528*x1*x1+18.600*x2*x2-0.537*x3*x3-2.062*x1*x2+0.769*x1*x3+0.243*x2*x3
            y2 = 8.655-2.581*x1-2.178*x2+12.716*x3+0.059*x1*x1+0.0496*x2*x2-0.074*x3*x3-0.021*x1*x2-0.0487*x1*x3+0.053*x2*x3
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
            y1 = 9803.455-382.115*x1-263.968*x2+1.917*x3+4.528*x1*x1+18.600*x2*x2-0.537*x3*x3-2.062*x1*x2+0.769*x1*x3+0.243*x2*x3
            y2 = 8.655-2.581*x1-2.178*x2+12.716*x3+0.059*x1*x1+0.0496*x2*x2-0.074*x3*x3-0.021*x1*x2-0.0487*x1*x3+0.053*x2*x3
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