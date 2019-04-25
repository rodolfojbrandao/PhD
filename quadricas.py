import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

for i in range(20, 51, 5):
    for j in range(20, 51, 5):
        for k in range(20, 51, 5):
            for l in range(10, 501, 5):
                for m in range(10, 501, 5):
                    a = i/10
                    b = j/10
                    c = k/10
                    n1 = l/100
                    n2 = m/100


                    name = ("A",a,"B",b,"C",c,"N1",n1,"N2",n2)


                    def quadric(x, y, z):
                        return ((x/a)**(2/n2)+(y/b)**(2/n2))**(n2/n1)+(z/c)**(2/n1)-1
                    fig = plt.figure()
                    ax = fig.add_subplot(111, projection='3d')

                    x_range = np.arange(-max(a, b, c), max(a, b, c), 100)
                    y_range = np.arange(-max(a, b, c), max(a, b, c), 100)
                    X, Y = np.meshgrid(x_range, y_range)

                    A = np.linspace(-max(a, b, c), max(a, b, c), 20)

                    A1, A2 = np.meshgrid(A, A)

                    for z in A:
                        X, Y = A1, A2
                        Z = quadric(X, Y, z)
                        ax.contour(X, Y, Z + z, [z], zdir='z', cmap=cm.coolwarm)
                    for y in A:
                        X, Z = A1, A2
                        Y = quadric(X, y, Z)
                        ax.contour(X, Y + y, Z, [y], zdir='y', cmap=cm.coolwarm)

                    for x in A:
                        Y, Z = A1, A2
                        X = quadric(x, Y, Z)
                        ax.contour(X + x, Y, Z, [x], zdir='x', cmap=cm.coolwarm)

                    ax.set_zlim3d(-max(a, b, c), max(a, b, c))
                    ax.set_xlim3d(-max(a, b, c), max(a, b, c))
                    ax.set_ylim3d(-max(a, b, c), max(a, b, c))
                    ax.set_title(name)
                    ax.set_xlabel('x')
                    ax.set_ylabel('y')
                    ax.set_zlabel('z')
                    plt.savefig('/home/rodolfo/Desktop/Imagens/{}.pdf'.format(name), transparent=True, bbox_inches='tight',dpi=600)
                    plt.close()