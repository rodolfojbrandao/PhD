# otimizacao jeniffer
import numpy as np

a = np.linspace(-1.4826,1.4826,99)

x1 = 0
x2 = 0
x3 = 0
x4 = 0

Y1=0

for i in range(0, len(a)):
    x1 = a[i]
    for j in range(0, len(a)):
        x2 = a[j]
        for k in range(0, len(a)):
            x3 = a[k]
            for l in range(0, len(a)):
                x4 = a[l]
                y1 = 78.2928-2.1087*(x1)+0.0649*(x1)*(x1)+6.0826*(x2)-2.8858*(x2)*(x2)+1.1355*(x3)-1.3479*(x3)*(x3)+4.4632*(x4)-2.1334*(x4)*(x4)-0.0277*(x1)*(x2)-0.1731*(x1)*(x3)+0.0804*(x1)*(x4)-0.0648*(x2)*(x3)-1.7892*(x2)*(x4)-0.4851*(x3)*(x4)
                if y1>Y1:
                    Y1 = y1.copy()
                    x1_maxi_y1 = x1
                    x2_maxi_y1 = x2
                    x3_maxi_y1 = x3
                    x4_maxi_y1 = x4

print('=============================================================================================')
print(' maximo de y1 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f}, x3 de {:.2f} e x4 de {:.2f}'.format(Y1,x1_maxi_y1,x2_maxi_y1,x3_maxi_y1,x4_maxi_y1))