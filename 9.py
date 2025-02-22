import numpy as np

#f = open("input.txt","r")
#s = f.readlines()

with open("input.txt") as f:
    s = f.read().splitlines()

s = s[0]

a=len(s)

diskMap = []
disk = []

for i in range(a):
    diskMap.append(int(s[i]))
    if i%2 == 0:
        disk.extend([i//2]*int(s[i]))
    else:
        disk.extend([-1] * int(s[i]))

l = len(disk)
diskList = [[-1,-1] for i in range(a)]

for i in range(a):
    diskList[i][0] = diskMap[i]

    if i%2==0:
        diskList[i][1] = i//2


def diskListSum(diskList):
    S=0
    for i in range(len(diskList)):
        S += diskList[i][0]
    return S
print(diskListSum(diskList))

for i in range(a):
    print(str(i) + "/" + str(a))
    for j in range(a-i-1):
        if diskList[a-i-1][0] == diskList[j][0] and diskList[a-i-1][1] > -1 and diskList[j][1] == -1:
            diskList[j][1] = diskList[a-i-1][1]
            diskList[a - i - 1][1] = -1

        elif diskList[a-i-1][0] < diskList[j][0] and diskList[a-i-1][1] > -1 and diskList[j][1] == -1:
            leftover = [diskList[j][0]-diskList[a-i-1][0], -1]
            diskList[j][1] = diskList[a - i - 1][1]
            diskList[j][0] = diskList[a-i-1][0]
            diskList[a - i - 1][1] = -1
            diskList[a - i - 1][0] += diskList[a - i - 2][0]

            for k in range(1,a-i-1-j):
                diskList[a-i-1-k] = diskList[a-i-2-k]
            diskList[j+1]=leftover

print(diskListSum(diskList))
S=0
t=0

for i in range(a):
    for k in range(diskList[i][0]):
        S += t*diskList[i][1]*(diskList[i][1]>-1)
        t += 1
print(S)
input()
