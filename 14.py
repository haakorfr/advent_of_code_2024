import numpy as np
from copy import deepcopy
from matplotlib import pyplot as plt
import matplotlib.animation as animation

with open("input.txt") as f:
    s = f.read().splitlines()

a = len(s)
b = len(s[0])
W = 101
H = 103


p1 = np.zeros(a,dtype = int)
p2 = np.zeros(a,dtype = int)
v1 = np.zeros(a,dtype = int)
v2 = np.zeros(a,dtype = int)

for i in range(len(s)):
    newP = np.array(s[i].split()[0][2:].split(","),dtype=int)
    p1[i] = newP[0]
    p2[i] = newP[1]
    newV = np.array(s[i].split()[1][2:].split(","),dtype=int)
    v1[i] = newV[0]
    v2[i] = newV[1]

def printRobots(p1,p2):
    M = np.zeros((W,H),dtype = int)
    for i in range(a):
        M[p1[i],p2[i]] += 1
    for j in range(H):
        for i in range(W):
            if M[i,j]:
                print(M[i,j],end="")
            else: print(".",end="")
        print()
    print()
def plotRobots(p1,p2):
    M = np.zeros((W,H),dtype = int)
    for i in range(a):
        M[p1[i],p2[i]] += 1
    plt.spy(M)
    plt.show()

#plotRobots(p1,p2)
#input()

fig, ax = plt.subplots()
scat = ax.scatter(p1, p2)
ax.set(xlim=[0, 101], ylim=[0, 103])
frame_text = ax.text(0.02, 0.9, '', transform=ax.transAxes, fontsize=12, color='red')

def update(frame):
    # for each frame, update the data stored on each artist.
    x = (p1 + frame*v1) % W
    y = (p2 + frame*v2) % H
    # update the scatter plot:
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    frame_text.set_text(f'Frame: {frame}')
    return scat, frame_text
ani = animation.FuncAnimation(fig=fig, func=update, frames=100, interval=50)
plt.show()

for i in range(100):
    p1 = (p1 + v1)%W
    p2 = (p2 + v2)%H
    printRobots(p1, p2)
    print(i+1)
    input()

printRobots(p1, p2)
input()

quad = [0,0,0,0]

for i in range(len(p1)):
    if p1[i] == W // 2 or p2[i] == H // 2:
        continue
    else:
        quad[(2 * p1[i]) // W + 2 * ((2 * p2[i]) // H)] += 1
print(quad)
print(np.prod(quad))


"""
p = (p + 100*v)%m
#print(p)
#printTiles(p)

if p[0] == 101//2 or p[1] == 103//2:
    #print("cont")
    continue
else:
    #print("quad: ", (2*p[0])//m[0]+ 2* ((2*p[1])//m[1]))
    quad[(2*p[0])//m[0]+ 2* ((2*p[1])//m[1])]+=1

#input()"""
