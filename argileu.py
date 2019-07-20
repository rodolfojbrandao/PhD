import numpy as np

a = np.linspace(-1.414,1.414,99)
b = np.linspace(-1.414,1.414,99)

x1 = 0
x2 = 0

y1=0

y1_maxi = 0.41-0.0075*(x1)+0.000125*(x1)*(x1)+0.03836*(x2)-0.070375*(x2)*(x2)-0.02*(x1)*(x2)
y1_mini = 0.41-0.0075*(x1)+0.000125*(x1)*(x1)+0.03836*(x2)-0.070375*(x2)*(x2)-0.02*(x1)*(x2)

x1_maxi_y1 = 0
x2_maxi_y1 = 0
x1_mini_y1 = 0
x2_mini_y1 = 0

for i in range(0, len(a)):
    x1 = a[i]
    for j in range(0, len(b)):
        x2 = b[j]
        y1 = 0.41-0.0075*(x1)+0.000125*(x1)*(x1)+0.03836*(x2)-0.070375*(x2)*(x2)-0.02*(x1)*(x2)
        if y1>y1_maxi:
            y1_maxi = y1
            x1_maxi_y1 = x1
            x2_maxi_y1 = x2
        elif y1<y1_mini:
            y1_mini = y1
            x1_mini_y1 = x1
            x2_mini_y1 = x2

print('=============================================================================================')
print(' maximo de y1 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f}'.format(y1_maxi,x1_maxi_y1,x2_maxi_y1))
print(' minimo de y1 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f}'.format(y1_mini,x1_mini_y1,x2_mini_y1))