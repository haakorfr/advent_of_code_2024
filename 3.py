f = open("input.txt","r")
s = f.readlines()


S = 0
t = 1

for linje in s:
    for i in range(len(linje) - 6):
        if linje[i:i+4] == "do()":
            t = 1
        if linje[i:i+7] == "don't()":
            t = 0
        if not linje[i:i+4] == "mul(":
            continue
        try:
            u = linje[i+4:].split(",",1)
            n = int(u[0])
            v = u[1].split(")",1)
            m = int(v[0])
            S += n*m*t
        except:
            continue


print(S)
