f = open("1_input.txt","r")
s = f.readlines()

l1 = []
l2 = []
for linje in s:
    linjeListe = linje.split()
    l1.append(int(linjeListe[0]))
    l2.append(int(linjeListe[1]))
l1.sort()
l2.sort()
PartOne = 0
PartTwo = 0

for i in range(len(l1)):
    PartOne += abs(l1[i]-l2[i])
    PartTwo += l2.count(l1[i])*l1[i]

print(PartOne)
print(PartTwo)
