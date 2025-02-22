import numpy as np

#f = open("input.txt","r")
#s = f.readlines()

with open("input.txt") as f:
    s = f.read().splitlines()

a=len(s)
b=len(s[0])

print(s)

def splitLinje(linje):
    m = []
    n = 0
    l = linje.split(":")
    n = int(l[0])
    m = l[1].split()
    for k in range(len(m)): m[k] = int(m[k])
    return n, m

def concatenate(a,b):
    return int(f"{a}{b}")

def evaluate(m,k):
    P=m[0]

    for i in range(1,len(m)):
        if k % 3 == 0:
            P += m[i]
        if k % 3 == 1:
            P *= m[i]
        if k % 3 == 2:
            P = concatenate(P,m[i])
        k = k//3
    return P


S=0

for linje in s:
    n,m = splitLinje(linje)
    for k in range(3**(len(m)-1)):
        if n == evaluate(m,k):
            S += n
            break
print(S)