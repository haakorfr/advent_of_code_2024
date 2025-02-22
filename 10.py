import numpy as np

#f = open("input.txt","r")
#s = f.readlines()

with open("input.txt") as f:
    s = f.read().splitlines()

a=len(s)
b=len(s[0])

MAP = np.zeros((a,b))
StartCoords = []
for i in range(a):
    for j in range(b):
        MAP[i,j] = int(s[i][j])
        if MAP[i,j] == 0:
            StartCoords.append([i,j])
"""
nStart = np.sum(MAP==0)

TailHeads = np.zeros((nStart, a,b), dtype=bool)

for k in range(nStart):
    TailHeads[(k,)+tuple(StartCoords[k])] = True


def iterate(TailHeads):
    for k in range(nStart):
        for i in range(a):
            for j in range(b):
                if TailHeads[k,i,j]:
                    try:
                        if  MAP[i+1,j] - MAP[i,j] == 1: TailHeads[k,i+1,j] = True
                    except: pass
                    try:
                        if  MAP[i,j+1] - MAP[i,j] == 1: TailHeads[k,i,j+1] = True
                    except: pass
                    try:
                        if i-1 >= 0:
                            if  MAP[i-1,j] - MAP[i,j] == 1: TailHeads[k,i-1,j] = True
                    except: pass
                    try:
                        if j-1 >= 0:
                            if  MAP[i,j-1] - MAP[i,j] == 1: TailHeads[k,i,j-1] = True
                    except: pass

for i in range(10):
    iterate(TailHeads)

S=0
for k in range(nStart):
    S += np.sum(MAP*TailHeads[k] == 9)
print(S)

#start på 0
#finn antall 1ere rundt = n
#legg til n paths.
#for hver path: kjør igjen

#def f(pos, M):
#   new_directions = de nye veiene å gå
#   return_data = tuple(new_directions[0],new_directions[1],....)
#   return tuple(pos) + f(new_directions[i],M) for i in range(len(new_directions)) Ikke helt...
"""


def f(pos,S):
    if pos[0]+1 < a:
        if MAP[pos[0]+1,pos[1]] - MAP[pos[0],pos[1]] == 1:
            if MAP[pos[0]+1,pos[1]] == 9:  S += 1
            else:   S= f([pos[0]+1,pos[1]],S)
    if pos[0] - 1 > -1:
        if MAP[pos[0]-1,pos[1]] - MAP[pos[0],pos[1]] == 1:
            if MAP[pos[0]-1,pos[1]] == 9:  S +=1
            else:   S=f([pos[0]-1,pos[1]],S)
    if pos[1] + 1 < b:
        if MAP[pos[0],pos[1]+1] - MAP[pos[0],pos[1]] == 1:
            if MAP[pos[0],pos[1]+1] == 9:  S +=1
            else:   S=f([pos[0],pos[1]+1],S)
    if pos[1] - 1 > -1:
        if MAP[pos[0],pos[1]-1] - MAP[pos[0],pos[1]] == 1:
            if MAP[pos[0],pos[1]-1] == 9:  S += 1
            else: S = f([pos[0],pos[1]-1],S)
    return S

S=0
for i in range(len(StartCoords)):
    print(i)
    S += f(StartCoords[i],0)
print(S)