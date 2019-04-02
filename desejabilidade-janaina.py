# otimizacao RL HC OX
import numpy as np

a = np.linspace(-1.41,1.41,99)
b = np.linspace(-1.41,1.41,99)
c = np.linspace(-1.41,1.41,99)

x1 = 0
x2 = 0
x3 = 0

y1=0
y2=0
d1=0
d2=0
d=0
D=0

y1_maxi = 45.206+1.391*x1-4.980*x1*x1+2.207*x2-3.066*x2*x2+7.075*x3-6.423*x3*x3-2.395*x1*x2 -2.736*x1*x3+1.270*x2*x3
y1_mini = 45.206+1.391*x1-4.980*x1*x1+2.207*x2-3.066*x2*x2+7.075*x3-6.423*x3*x3-2.395*x1*x2 -2.736*x1*x3+1.270*x2*x3
y2_maxi = 8.825 -4.974*x1 +6.695*x1*x1 -0.018*x2 -0.621*x2*x2-1.674*x3+3.279*x3*x3+4.210*x1*x2-2.640*x1*x3-4.423*x2*x3
y2_mini = 8.825 -4.974*x1 +6.695*x1*x1 -0.018*x2 -0.621*x2*x2-1.674*x3+3.279*x3*x3+4.210*x1*x2-2.640*x1*x3-4.423*x2*x3

x1_maxi_y1 = 0
x2_maxi_y1 = 0
x3_maxi_y1 = 0
x1_mini_y1 = 0
x2_mini_y1 = 0
x3_mini_y1 = 0
x1_maxi_y2 = 0
x2_maxi_y2 = 0
x3_maxi_y2 = 0
x1_mini_y2 = 0
x2_mini_y2 = 0
x3_mini_y2 = 0

for i in range(0, len(a)):
    x1 = a[i]
    for j in range(0, len(b)):
        x2 = b[j]
        for k in range(0, len(c)):
            x3 = c[k]
            y1 = 45.206+1.391*x1-4.980*x1*x1+2.207*x2-3.066*x2*x2+7.075*x3-6.423*x3*x3-2.395*x1*x2 -2.736*x1*x3+1.270*x2*x3
            y2 = 8.825 -4.974*x1 +6.695*x1*x1 -0.018*x2 -0.621*x2*x2-1.674*x3+3.279*x3*x3+4.210*x1*x2-2.640*x1*x3-4.423*x2*x3
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
            y1 = 45.206+1.391*x1-4.980*x1*x1+2.207*x2-3.066*x2*x2+7.075*x3-6.423*x3*x3-2.395*x1*x2 -2.736*x1*x3+1.270*x2*x3
            y2 = 8.825 -4.974*x1 +6.695*x1*x1 -0.018*x2 -0.621*x2*x2-1.674*x3+3.279*x3*x3+4.210*x1*x2-2.640*x1*x3-4.423*x2*x3
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