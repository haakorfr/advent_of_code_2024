f = open("input.txt","r")
s = f.readlines()


S = 0

def isGood(l):
    t = 0  # Denne er 1 hvis sekvensen er nedadgående og -1 dersom den er oppadgående.7
    s = 0
    for i in range(len(l) - 1):
        n = int(l[i])
        m = int(l[i + 1])
        if n - m == 0:
            return i
        if abs(n - m) > 3:
            return i
        if t == 0:
            if n - m > 0:
                t = 1
            else:
                t = -1
            continue
        if n - m > 0:
            s = 1
        else:
            s = -1
        if s * t == -1:
            return i
        if i == len(l) - 2:
            return -1
    print("isGood error")


for linje in s:
    linjeListe = linje.split()
    t = isGood(linjeListe)
    if t == -1:
        S+=1
        #print(linjeListe)
        #input()
        continue

    linjeListeCopy = linjeListe.copy()
    linjeListeCopy.pop(t)
    s = isGood(linjeListeCopy)

    if s == -1:
        S += 1
        #print(linjeListe,linjeListeCopy)
        #input()
        continue
    linjeListeCopy = linjeListe.copy()
    linjeListeCopy.pop(t+1)
    s = isGood(linjeListeCopy)

    if s == -1:
        S += 1
        #print(linjeListe,linjeListeCopy)
        #input()
        continue

    if t > 0:
        linjeListeCopy = linjeListe.copy()
        linjeListeCopy.pop(t-1)
        s = isGood(linjeListeCopy)

        if s == -1:
            S += 1
            # print(linjeListe,linjeListeCopy)
            # input()
            continue

print(S)
