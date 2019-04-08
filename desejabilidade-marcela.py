# otimizacao RL HC OX
import numpy as np

a = [20,25,30,35,40]
b = [6, 9, 12, 15]
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

y1_maxi = 8974.661-339.130*x1-206.667*x2+9.389*x3+3.858*x1*x1+11.755*x2*x2-0.617*x3*x3-1.048*x1*x2+0.656*x1*x3+0.314*x2*x3
y1_mini = 8974.661-339.130*x1-206.667*x2+9.389*x3+3.858*x1*x1+11.755*x2*x2-0.617*x3*x3-1.048*x1*x2+0.656*x1*x3+0.314*x2*x3
y2_maxi = -56.7096-0.1061*x1+4.1043*x2+13.4952*x3+0.0308*x1*x1-0.1246*x2*x2-0.0701*x3*x3-0.0998*x1*x2-0.0575*x1*x3-0.0157*x2*x3
y2_mini = -56.7096-0.1061*x1+4.1043*x2+13.4952*x3+0.0308*x1*x1-0.1246*x2*x2-0.0701*x3*x3-0.0998*x1*x2-0.0575*x1*x3-0.0157*x2*x3

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
            y1 = 8974.661-339.130*x1-206.667*x2+9.389*x3+3.858*x1*x1+11.755*x2*x2-0.617*x3*x3-1.048*x1*x2+0.656*x1*x3+0.314*x2*x3
            y2 = -56.7096-0.1061*x1+4.1043*x2+13.4952*x3+0.0308*x1*x1-0.1246*x2*x2-0.0701*x3*x3-0.0998*x1*x2-0.0575*x1*x3-0.0157*x2*x3
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
            y1 = 8974.661-339.130*x1-206.667*x2+9.389*x3+3.858*x1*x1+11.755*x2*x2-0.617*x3*x3-1.048*x1*x2+0.656*x1*x3+0.314*x2*x3
            y2 = -56.7096-0.1061*x1+4.1043*x2+13.4952*x3+0.0308*x1*x1-0.1246*x2*x2-0.0701*x3*x3-0.0998*x1*x2-0.0575*x1*x3-0.0157*x2*x3
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
