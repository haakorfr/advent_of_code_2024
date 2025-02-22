import numpy as np

#f = open("input.txt","r")
#s = f.readlines()

with open("input.txt") as f:
    s = f.read().splitlines()

a=len(s)
b=len(s[0])

startingPos = np.array([0,0])
startingDir = np.array([0,0])
startingDirNumber = 0
obstructions = np.zeros((a,b),dtype = bool)

for i in range(a):
    for j in range(b):
        if s[i][j] == "^":
            startingDir = np.array([-1,0])
            startingDirNumber = 0
            startingPos = np.array([i,j])
        if s[i][j] == ">":
            startingDir = np.array([0,1])
            startingDirNumber = 1
            startingPos = np.array([i, j])
        if s[i][j] == "v":
            startingDir = np.array([1,0])
            startingDirNumber = 2
            startingPos = np.array([i, j])
        if s[i][j] == "<":
            startingDir = np.array([0,-1])
            startingDirNumber = 3
            startingPos = np.array([i, j])
        if s[i][j] == "#": obstructions[i,j] = True

M = np.zeros((a,b),dtype=bool)
M[tuple(startingPos)]= True
R = np.array([[0,1],[-1,0]])

pos = np.copy(startingPos)
dir = np.copy(startingDir)

def printM(M):
    for i in range(a):
        for j in range(b):
            if s[i][j] == "#": print("#",end="")
            elif M[i,j]: print("X",end="")
            else: print(".",end="")
        print()


while True:
    try:
        newpos = pos + dir
        if newpos[0] < 0 or newpos[1] < 0: break
        if s[newpos[0]][newpos[1]] == "#":
            dir = R@dir
        else:
            pos = newpos
            M[tuple(pos)] = True
    except:
        break
#printM(M)

print(np.sum(M))

# for hvert felt i M, bortsett fra starting pos, legg til en obstruction der.
# så kjør containsLoop(M, startingPos, obstructions)
# denne recorder pos og dir i arrays PosxDir. dersom pos,dir in PosxDir, så har vi en loop: return True
# ellers kjøres til index out of range, i.e. except : return False

def containsLoop(obstructions,q=0):
    def printPosDir(PosDir):
        for i in range(a):
            for j in range(b):
                if obstructions[i,j]:
                    print("#", end="")
                elif np.sum(PosDir[i, j]):
                    print("X", end="")
                else:
                    print(".", end="")
            print()

    def directionNumberToVector(direction):
        if direction == 0: return np.array([-1,0])
        if direction == 1: return np.array([0,1])
        if direction == 2: return np.array([1,0])
        if direction == 3: return np.array([0,-1])

    PosDir = np.zeros((a,b,4),dtype = bool) #Denne angir faserommet. [i,j,k] angir (i,j) posisjon, og k retning.
    PosDir[tuple(startingPos)][startingDirNumber] = True
    if q: print(startingPos,startingDirNumber)
    direction = startingDirNumber
    position = startingPos
    while True:
        if q:
            printPosDir(PosDir)
            input()
        newpos = position + directionNumberToVector(direction)
        if newpos[0] < 0 or newpos[1] < 0 or newpos[0]>=a or newpos[1] >= b: return False
        if obstructions[tuple(newpos)]: direction = (direction + 1)%4
        else:
            position = newpos
        if PosDir[tuple(position)][direction]:
            if q:
                print(position,direction)
            return True
        else:
            PosDir[tuple(position)][direction] = True


t = 0
for i in range(a):
    print(i)
    for j in range(b):
        if (not (i == startingPos[0] and j == startingPos[1])) and M[i,j]:
            #print("hei")
            obstructions[i, j] = True
            t += containsLoop(obstructions)
            #if containsLoop(obstructions):
            #    containsLoop(obstructions,1)
            obstructions[i,j] = False

print(t)