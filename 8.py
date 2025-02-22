import numpy as np

#f = open("input.txt","r")
#s = f.readlines()

with open("input.txt") as f:
    s = f.read().splitlines()

a=len(s)
b=len(s[0])


Antennas = dict()

for i in range(a):
    for j in range(b):
        if not s[i][j] == ".":
            if not s[i][j] in Antennas.keys() :
                Antennas[s[i][j]] = [[i,j]] #np.zeros((a,b),dtype = bool)
            else:
                Antennas[s[i][j]].append([i,j])

Antinodes = np.zeros((a,b),dtype = bool)
AntinodeCoords = []

#print(Antennas)


for key, value in Antennas.items():
    Antennas[key] = np.array(Antennas[key])
#print(Antennas)

for key, value in Antennas.items():
    for i in range(len(value)-1):
        for j in range(i+1,len(value)):
            N = max(a,b)//np.max(np.abs(value[i]-value[j]))
            for n in range(-N,N):
                if np.prod((1+n)*value[i] - n*value[j] >= 0) and np.prod((1+n)*value[i] - n*value[j] < np.array([a,b])):
                    AntinodeCoords.append((1+n)*value[i] - n*value[j])

for u in AntinodeCoords:
    try:
        Antinodes[tuple(u)] = True
    except:
        continue

print(np.array(Antinodes,dtype=int))
print(Antinodes.sum())
