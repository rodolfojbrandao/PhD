import numpy as np
import math

T1 = 100
T2 = 500
Lx = 3
Ly = 1
ny = 2
nx = 100

a = 1
b = 0.5
c = 0.5

dados = np.zeros((ny*nx,3))
L = np.zeros((nx,1))
L[0]=0
L[nx-1]=Lx

P = np.zeros((nx,1))
Q = np.zeros((nx,1))
Q[0]=T1
Q[nx-1]=T2
T = np.zeros((nx,1))
T[0]=T1
T[nx-1]=T2

for i in range (1,nx-1):
    P[i]=b/(a-c*P[i-1])
    Q[i]=c*Q[i-1]/(a-c*P[i-1])
    L[i]=Lx/nx*i

for i in range (nx-1,1,-1):
    T[i-1]=P[i-1]*T[i]+Q[i-1]

dados[:nx,0] = L[:,0]
dados[:nx,1] = 0
dados[:nx,2] = T[:,0]

dados[nx:ny*nx,0] = L[:,0]
dados[nx:ny*nx,1] = 1
dados[nx:ny*nx,2] = T[:,0]

np.savetxt('A_data.dat', dados)
