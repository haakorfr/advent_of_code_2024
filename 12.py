import numpy as np
from copy import deepcopy

with open("input.txt") as f:
    s = f.read().splitlines()

a = len(s)
b = len(s[0])

"""
Map = np.zeros((a,b),dtype=int)
downShiftedMap = np.zeros((a,b),dtype=int)
upShiftedMap = np.zeros((a,b),dtype=int)
leftShiftedMap = np.zeros((a,b),dtype=int)
rightShiftedMap = np.zeros((a,b),dtype=int)
#uprightShiftedMap = np.zeros((a,b),dtype=int)
#upleftShiftedMap = np.zeros((a,b),dtype = int)
#downleftShiftedMap = np.zeros((a,b),dtype =int)
#downrightShiftedMap = np.zeros((a,b),dtype=int)

for i in range(a):
    for j in range(b):
        Map[i,j] = ord(s[i][j]) - ord("A") + 1
        if 0 <= i-1: downShiftedMap[i,j] = ord(s[i-1][j]) - ord("A") + 1
        if i+1 < a: upShiftedMap[i,j] = ord(s[i+1][j]) - ord("A") + 1
        if j+1 < b: leftShiftedMap[i,j] = ord(s[i][j+1]) - ord("A") + 1
        if 0 <= j-1: rightShiftedMap[i,j] = ord(s[i][j-1]) - ord("A") + 1
        #if i+1 < a and j+1 < b: upleftShiftedMap[i,j] = ord(s[i+1][j+1]) - ord("A") + 1
        #if i+1 < a and 0 <= j-1: uprightShiftedMap[i,j] = ord(s[i+1][j-1]) - ord("A") + 1
        #if 0<= i-1 and j+1 < b: downleftShiftedMap[i,j] = ord(s[i-1][j+1]) - ord("A") + 1
        #if 0 <= i-1 and 0 <= j-1: downrightShiftedMap[i,j] = ord(s[i-1][j-1]) - ord("A") + 1

print(Map)
print(downShiftedMap)
print(np.array( downShiftedMap != Map,dtype = int))
"""


# the operation that grows the region M is the sum of linear transformations
# moving one step to the right, left diagonal etc. can be described by a lin. trans.
# Use Map as one big vector and then shift by this lin trans.

# The linear transformation that shifts one up,

# [ 1,2,3,              [ 4,5,6,
#   4,5,6,      ->        7,8,9,
#   7,0,9 ]               0,0,0 ]

#   is given by

#              a*b
#  -------------|------------
#      b
#   ---|---
#   0, 0, 0, 1, 0, 0, 0, 0, 0,
#   0, 0, 0, 0, 1, 0, 0, 0, 0,
#   0, 0, 0, 0, 0, 1, 0, 0, 0,
#   0, 0, 0, 0, 0, 0, 1, 0, 0,
#   0, 0, 0, 0, 0, 0, 0, 1, 0,
#   0, 0, 0, 0, 0, 0, 0, 0, 1,
#   0, 0, 0, 0, 0, 0, 0, 0, 0,
#   0, 0, 0, 0, 0, 0, 0, 0, 0,
#   0, 0, 0, 0, 0, 0, 0, 0, 0,

# Likewise, shifting one down is given by a left shifted diagonal.
# Shifting left is

# [ 1,2,3,              [ 2,3,0,
#   4,5,6,      ->        5,6,0,
#   7,0,9 ]               8,9,0 ]

# which is given by

#      1   b-1  1   b-1  1   b-1
#      |  --|-- |  --|-- |  --|--
#      0, 1, 0, 0, 0, 0, 0, 0, 0,
#      0, 0, 1, 0, 0, 0, 0, 0, 0,
#      0, 0, 0, 0, 0, 0, 0, 0, 0,
#      0, 0, 0, 0, 1, 0, 0, 0, 0,
#      0, 0, 0, 0, 0, 1, 0, 0, 0,
#      0, 0, 0, 0, 0, 0, 0, 0, 0,
#      0, 0, 0, 0, 0, 0, 0, 1, 0,
#      0, 0, 0, 0, 0, 0, 0, 0, 1,
#      0, 0, 0, 0, 0, 0, 0, 0, 0,

#Thus we prepare:

#u = np.array([0,1,0],dtype = bool)
#v = np.array([1,1,0],dtype = bool)
#print(v != u)
#input()

a=a+2
b=b+2

Map = np.zeros((a*b),dtype = int)
for i in range(a-2):
    for j in range(b-2):
        Map[(i+1)*b+j+1] = ord(s[i][j]) - ord("A") + 1


leftShift = np.eye(a*b,a*b,1,dtype=bool) #diagonal shifted one up
rightShift = np.eye(a*b,a*b,-1,dtype=bool)
upShift = np.eye(a*b,a*b,b,dtype=bool)
downShift = np.eye(a*b,a*b,-b,dtype=bool)
for k in range(1,a):
    leftShift[k*b -1 , k*b] = 0
    rightShift[k*b, k*b-1] = 0

growMap = leftShift + rightShift + upShift + downShift + np.eye(a*b,a*b,dtype=bool)
#test = np.array([1,2,3,4,5,6,7,8,9])
#print(leftShift)
#print(rightShift)
#print(upShift)
#print(downShift)
#print(leftShift@test)
#print(rightShift@test)
#print(upShift@test)
#print(downShift@test)

def printMap(M, displayBool=False,displayLetters = False):
    for i in range(a):
        for j in range(b):
            if displayBool:
                print(int(bool(M[i * b + j])), end=" ")
            elif displayLetters:
                if M[i * b + j] == 0:
                    print(0,end=" ")
                else:
                    print(chr(M[i * b + j]+ord("A")-1), end=" ")
            else:
                print(int(M[i*b + j]), end=" ")
        print()
    print()

"""
def region(i,j):
    M = np.zeros(a*b,dtype=int)
    n = Map[i*b +j]
    M[i*b + j] = 1
    def iterate(M):
        tempM = np.zeros(a*b,dtype=int)
        tempM = (growMap@M > 0)
        border = tempM - M

        M += (border*Map == n)
        return M

    newM = np.zeros(a * b, dtype=int)
    while np.sum(np.abs(M-newM)) > 0:
        newM = np.copy(M)
        M=iterate(M)
    return M

regions = []

for i in range(a):
    print(i)
    for j in range(b):
        print(j)
        if Map[i*b +j]:
            regions.append(region(i,j))
            Map = Map*(1-regions[-1])


for i in range(len(regions)):
    printMap(regions[i])
    input()
"""

def price_of_region(region):
    region = np.array(region,dtype = int)
    #boundary = (growMap @ region)*(1-region)
    #printMap(boundary)
    #return np.sum(region) * np.sum(boundary)

    S=0

    boundary = (upShift @ region)*(1-region)
    boundary = (rightShift @ boundary) * (1 - boundary)
    S += np.sum(boundary)

    boundary = (downShift @ region) * (1 - region)
    boundary = (rightShift @ boundary) * (1 - boundary)
    S += np.sum(boundary)

    boundary = (rightShift @ region) * (1 - region)
    boundary = (downShift @ boundary) * (1 - boundary)
    S += np.sum(boundary)

    boundary = (leftShift @ region) * (1 - region)
    boundary = (downShift @ boundary) * (1 - boundary)
    S += np.sum(boundary)

    return np.sum(region) * S


def make_region(Map,i):
    region1 = np.zeros_like(Map)
    region2 = np.zeros_like(Map)

    region1[i] = 1
    #printMap(region1, displayBool=True)
    t=0
    while np.sum(region1 != region2):
        region2 = region1
        region1 = (region1 | growMap@region1)*Map
        t+=1
    return region1


def get_price_of_map(Map):
    #region = np.zeros_like(Map,dtype=bool)
    price = 0
    for i in range(a*b):
        if Map[i]:
            print(i, a * b)

            region = make_region(Map==Map[i],i)
            Map = Map * (~ region)
            #printMap(region,displayBool=True)
            #printMap(Map)
            #calculate the price
            price += price_of_region(region)
            #print("hei")
            #input()
    return price
S=0
printMap(Map,displayLetters=True)
S += get_price_of_map(Map)

print(S)

