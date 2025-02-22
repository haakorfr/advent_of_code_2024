import numpy as np
from copy import deepcopy

with open("input.txt") as f:
    s = f.read().splitlines()

a = len(s)
b = len(s[0])

def price(M, x):
    D = M[0,0]*M[1,1]-M[1,0]*M[0,1]
    if D==0:
        print("determinant problem")
    M_inv = np.array([[M[1,1],-M[0,1]],
                      [-M[1,0],M[0,0]]],dtype = int)

    x += 10000000000000

    if  np.all(M@ (M_inv @ x //D) == x):
        return M_inv @ x // D

    else: return np.array([-1,-1])
M = np.zeros((2,2),dtype = int)
x = np.zeros(2,dtype = "object")
S = 0
for i in range(a-2):
    if len(s[i])>0:
        if s[i][0]=="B" and s[i+1][0]=="B":
            M[0,0] = int(s[i][12:14])
            M[1,0] = int(s[i][18:20])
            M[0,1] = int(s[i+1][12:14])
            M[1,1] = int(s[i+1][18:20])
            x[0]=int(s[i+2].split()[1][2:-1])
            x[1]=int(s[i+2].split()[2][2:])
            p = price(M,x)
            if p[0]==-1:
                continue
            else:
                S += p[0]*3 + p[1]

print(S)