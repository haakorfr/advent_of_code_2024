import numpy as np

f = open("input.txt","r")
s = f.readlines()

M = np.zeros((100,100),dtype=int)
t = 0

for line in s:
    try:
        M[int(line[0:2])][int(line[3:5])] = 1
    except:
        break
    t+=1

def order(tallListe):
    tempString = ""
    for k in range(len(tallListe)-1):
        for j in range(1, len(tallListe)-k):
            #print(k,k+j)
            if not M[int(tallListe[k])][int(tallListe[k+j])]:
                tempString = tallListe[k]
                tallListe[k] = tallListe[k+j]
                tallListe[k+j] = tempString
    return tallListe

def isOrdered(tallListe):
    for k in range(len(tallListe)-1):
        for j in range(1, len(tallListe)-k):
            #print(k,k+j)
            if not M[int(tallListe[k])][int(tallListe[k+j])]:
                return False
    return True


S=0
q = 0
tempString = ""
for i in range(t+1, len(s)):
    tallListe = s[i].strip("\n").split(",")

    if isOrdered(tallListe): continue

    #print(tallListe)
    #print(isOrdered(tallListe))
    #input()
    while not isOrdered(tallListe): tallListe = order(tallListe)
    #print(tallListe)
    #print(isOrdered(tallListe))
    #input()

    #print(s[i])
    #print(tallListe)
    #input()
    S += int(tallListe[len(tallListe)//2])
    #print(s[i])
    #print(int(tallListe[len(tallListe)//2]))
    #input()

print(S)