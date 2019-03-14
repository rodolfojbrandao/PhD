# otimizacao RL HC OX
import numpy as np

a = np.linspace(-1.7112,1.7112,99)
b = np.linspace(-1.7112,1.7112,99)
c = np.linspace(-1.7112,1.7112,99)

x1 = 0
x2 = 0
x3 = 0

y1=0
y2=0
d1=0
d2=0
d=0
D=0

y1_maxi = 12.77442-0.53491*(x1)-0.50509*(x1)*(x1)+1.46871*(x2)-1.42716*(x2)*(x2)+1.64515*(x3)-0.74927*(x3)*(x3)-1.315*(x1)*(x2)-0.4825*(x1)*(x3)+0.3*(x2)*(x3)
y1_mini = 12.77442-0.53491*(x1)-0.50509*(x1)*(x1)+1.46871*(x2)-1.42716*(x2)*(x2)+1.64515*(x3)-0.74927*(x3)*(x3)-1.315*(x1)*(x2)-0.4825*(x1)*(x3)+0.3*(x2)*(x3)
y2_maxi = 84.9927-21.7953*(x1)+7.8611*(x1)*(x1)-17.5615*(x2)-0.6766*(x2)*(x2)-12.9266*(x3)-0.6766*(x3)*(x3)-1.8750*(x1)*(x2)-0.6250*(x1)*(x3)+0.6250*(x2)*(x3)
y2_mini = 84.9927-21.7953*(x1)+7.8611*(x1)*(x1)-17.5615*(x2)-0.6766*(x2)*(x2)-12.9266*(x3)-0.6766*(x3)*(x3)-1.8750*(x1)*(x2)-0.6250*(x1)*(x3)+0.6250*(x2)*(x3)
y3_maxi = 7.39510-0.42804*(x1)-0.39285*(x1)*(x1)+0.63088*(x2)-1.08440*(x2)*(x2)+0.70166*(x3)-0.7378*(x3)*(x3)-0.7425*(x1)*(x2)-0.3875*(x1)*(x3)+0.14*(x2)*(x3)
y3_mini = 7.39510-0.42804*(x1)-0.39285*(x1)*(x1)+0.63088*(x2)-1.08440*(x2)*(x2)+0.70166*(x3)-0.7378*(x3)*(x3)-0.7425*(x1)*(x2)-0.3875*(x1)*(x3)+0.14*(x2)*(x3)
y4_maxi = 0.226077-0.025938*(x1)+0.0003*(x1)*(x1)+0.0127*(x2)-0.030367*(x2)*(x2)+0.014054*(x3)-0.0184*(x3)*(x3)-0.0225*(x1)*(x2)-0.0122*(x1)*(x3)+0.0015*(x2)*(x3)
y4_mini = 0.226077-0.025938*(x1)+0.0003*(x1)*(x1)+0.0127*(x2)-0.030367*(x2)*(x2)+0.014054*(x3)-0.0184*(x3)*(x3)-0.0225*(x1)*(x2)-0.0122*(x1)*(x3)+0.0015*(x2)*(x3)
y5_maxi = 0.155176+0.02395*(x1)-0.01824*(x1)*(x1)+0.0365*(x2)-0.0107*(x2)*(x2)+0.03683*(x3)+0.004127*(x3)*(x3)+0.0108*(x1)*(x2)+0.00637*(x1)*(x3)-0.000125*(x2)*(x3)
y5_mini = 0.155176+0.02395*(x1)-0.01824*(x1)*(x1)+0.0365*(x2)-0.0107*(x2)*(x2)+0.03683*(x3)+0.004127*(x3)*(x3)+0.0108*(x1)*(x2)+0.00637*(x1)*(x3)-0.000125*(x2)*(x3)

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
x1_maxi_y3 = 0
x2_maxi_y3 = 0
x3_maxi_y3 = 0
x1_mini_y3 = 0
x2_mini_y3 = 0
x3_mini_y3 = 0
x1_maxi_y4 = 0
x2_maxi_y4 = 0
x3_maxi_y4 = 0
x1_mini_y4 = 0
x2_mini_y4 = 0
x3_mini_y4 = 0
x1_maxi_y5 = 0
x2_maxi_y5 = 0
x3_maxi_y5 = 0
x1_mini_y5 = 0
x2_mini_y5 = 0
x3_mini_y5 = 0





for i in range(0, len(a)):
    x1 = a[i]
    for j in range(0, len(b)):
        x2 = b[j]
        for k in range(0, len(c)):
            x3 = c[k]
            y1 = 12.77442-0.53491*(x1)-0.50509*(x1)*(x1)+1.46871*(x2)-1.42716*(x2)*(x2)+1.64515*(x3)-0.74927*(x3)*(x3)-1.315*(x1)*(x2)-0.4825*(x1)*(x3)+0.3*(x2)*(x3)
            y2 = 84.9927-21.7953*(x1)+7.8611*(x1)*(x1)-17.5615*(x2)-0.6766*(x2)*(x2)-12.9266*(x3)-0.6766*(x3)*(x3)-1.8750*(x1)*(x2)-0.6250*(x1)*(x3)+0.6250*(x2)*(x3)
            y3 = 7.39510-0.42804*(x1)-0.39285*(x1)*(x1)+0.63088*(x2)-1.08440*(x2)*(x2)+0.70166*(x3)-0.7378*(x3)*(x3)-0.7425*(x1)*(x2)-0.3875*(x1)*(x3)+0.14*(x2)*(x3)
            y4 = 0.226077-0.025938*(x1)+0.0003*(x1)*(x1)+0.0127*(x2)-0.030367*(x2)*(x2)+0.014054*(x3)-0.0184*(x3)*(x3)-0.0225*(x1)*(x2)-0.0122*(x1)*(x3)+0.0015*(x2)*(x3)
            y5 = 0.155176+0.02395*(x1)-0.01824*(x1)*(x1)+0.0365*(x2)-0.0107*(x2)*(x2)+0.03683*(x3)+0.004127*(x3)*(x3)+0.0108*(x1)*(x2)+0.00637*(x1)*(x3)-0.000125*(x2)*(x3)
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
            if y3 > y3_maxi:
                y3_maxi = y3
                x1_maxi_y3 = x1
                x2_maxi_y3 = x2
                x3_maxi_y3 = x3
            elif y3 < y3_mini:
                y3_mini = y3
                x1_mini_y3 = x1
                x2_mini_y3 = x2
                x3_mini_y3 = x3
            if y4 > y4_maxi:
                y4_maxi = y4
                x1_maxi_y4 = x1
                x2_maxi_y4 = x2
                x3_maxi_y4 = x3
            elif y4 < y4_mini:
                y3_mini = y4
                x1_mini_y4 = x1
                x2_mini_y4 = x2
                x3_mini_y4 = x3
            if y5 > y5_maxi:
                y5_maxi = y5
                x1_maxi_y4 = x1
                x2_maxi_y4 = x2
                x3_maxi_y4 = x3
            elif y5 < y5_mini:
                y3_mini = y5
                x1_mini_y5 = x1
                x2_mini_y5 = x2
                x3_mini_y5 = x3

print('=============================================================================================')
print(' maximo de y1 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y1_maxi,x1_maxi_y1,x2_maxi_y1,x3_maxi_y1))
print(' minimo de y1 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y1_mini,x1_mini_y1,x2_mini_y1,x3_mini_y1))
print('=============================================================================================')
print(' maximo de y2 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y2_maxi,x1_maxi_y2,x2_maxi_y2,x3_maxi_y2))
print(' minimo de y2 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y2_mini,x1_mini_y2,x2_mini_y2,x3_mini_y2))
print('=============================================================================================')
print(' maximo de y3 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y3_maxi,x1_maxi_y3,x2_maxi_y3,x3_maxi_y3))
print(' minimo de y3 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y3_mini,x1_mini_y3,x2_mini_y3,x3_mini_y3))
print('=============================================================================================')
print(' maximo de y4 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y4_maxi,x1_maxi_y4,x2_maxi_y4,x3_maxi_y4))
print(' minimo de y4 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y4_mini,x1_mini_y4,x2_mini_y4,x3_mini_y4))
print('=============================================================================================')
print(' maximo de y5 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y5_maxi,x1_maxi_y5,x2_maxi_y5,x3_maxi_y5))
print(' minimo de y5 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y5_mini,x1_mini_y5,x2_mini_y5,x3_mini_y5))

for i in range(0, len(a)):
    x1 = a[i]
    for j in range(0, len(b)):
        x2 = b[j]
        for k in range(0, len(c)):
            x3 = c[k]
            y1 = 12.77442-0.53491*(x1)-0.50509*(x1)*(x1)+1.46871*(x2)-1.42716*(x2)*(x2)+1.64515*(x3)-0.74927*(x3)*(x3)-1.315*(x1)*(x2)-0.4825*(x1)*(x3)+0.3*(x2)*(x3)
            y2 = 84.9927-21.7953*(x1)+7.8611*(x1)*(x1)-17.5615*(x2)-0.6766*(x2)*(x2)-12.9266*(x3)-0.6766*(x3)*(x3)-1.8750*(x1)*(x2)-0.6250*(x1)*(x3)+0.6250*(x2)*(x3)
            y3 = 7.39510-0.42804*(x1)-0.39285*(x1)*(x1)+0.63088*(x2)-1.08440*(x2)*(x2)+0.70166*(x3)-0.7378*(x3)*(x3)-0.7425*(x1)*(x2)-0.3875*(x1)*(x3)+0.14*(x2)*(x3)
            y4 = 0.226077-0.025938*(x1)+0.0003*(x1)*(x1)+0.0127*(x2)-0.030367*(x2)*(x2)+0.014054*(x3)-0.0184*(x3)*(x3)-0.0225*(x1)*(x2)-0.0122*(x1)*(x3)+0.0015*(x2)*(x3)
            y5 = 0.155176+0.02395*(x1)-0.01824*(x1)*(x1)+0.0365*(x2)-0.0107*(x2)*(x2)+0.03683*(x3)+0.004127*(x3)*(x3)+0.0108*(x1)*(x2)+0.00637*(x1)*(x3)-0.000125*(x2)*(x3)
            d1=(y1-y1_mini)/(y1_maxi-y1_mini) #maximizar
            d2=(y2-y2_mini)/(y2_maxi-y2_mini) #maximizar
            d3=(y3-y3_mini)/(y3_maxi-y3_mini) #maximizar
            d4=(y4-y4_mini)/(y4_maxi-y4_mini) #maximizar
            d5=(y5_maxi-y5)/(y5_maxi-y5_mini) #minimizar
            d=d1*d2*d3*d4*d5

            if d > D:
                D = d
                x1_opt = x1
                x2_opt = x2
                x3_opt = x3
                y1_opt=y1
                y2_opt=y2
                y3_opt=y3
                y4_opt=y4
                y5_opt=y5

print('=============================================================================================')
print(' ponto otimo com valor de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(D,x1_opt,x2_opt,x3_opt))
print(' y1 com valor de {:.2f} com y2 de {:.2f}'.format(y1_opt))
print(' y2 com valor de {:.2f} com y2 de {:.2f}'.format(y2_opt))
print(' y3 com valor de {:.2f} com y2 de {:.2f}'.format(y3_opt))
print(' y4 com valor de {:.2f} com y2 de {:.2f}'.format(y4_opt))
print(' y5 com valor de {:.2f} com y2 de {:.2f}'.format(y5_opt))


