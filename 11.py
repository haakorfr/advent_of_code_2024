import numpy as np
from copy import deepcopy

#f = open("input.txt","r")
#s = f.readlines()

with open("input.txt") as f:
    s = f.read().splitlines()

a=len(s)
b=len(s[0])

L = s[0].split()
global_stone_dict = dict()

unique_stones = list(set(L))
for i in range(len(unique_stones)):
    global_stone_dict[unique_stones[i]] = L.count(unique_stones[i])

print(global_stone_dict)


def blink(initial_dict: dict):
    new_stone_dict = {}
    for stone, multiplicity in initial_dict.items():
        new_stones = stone_blink(stone)
        for new_stone in new_stones:
            try:
                new_stone_dict[new_stone] += multiplicity
            except KeyError:
                new_stone_dict[new_stone] = multiplicity
    return new_stone_dict





def stone_blink(stone: str):
    l = len(stone)
    if stone == "0":
        return ["1"]
    elif l%2==0:
        return [str(int(stone[:l//2])), str(int(stone[l//2:]))]
    else:
        return [str(int(stone)*2024)]



"""       
        
def blink(L):
    nEven = 0
    S = set(L)
    
    M = [0]*len(S)
    for i in range(len(S)):
        M[i] = L.count(S[i])
    
    
    newL = []
    for i in range(len(L)):
        s = str(L[i])
        l = len(s)
        if L[i] == 0:
            newL.append(1)
        elif l%2==0:
            newL.append(int(s[:l//2]))
            newL.append(int(s[l//2:]))
        else:
            newL.append(L[i]*2024)
    return newL"""


for i in range(75):
    print(str(i) + "/" + "75")
    global_stone_dict = blink(global_stone_dict)
    print(global_stone_dict)
    #input()

mult_sum = sum(global_stone_dict.values())
print(mult_sum)

