f = open("input.txt","r")
s = f.readlines()

t = 0
for i in range(len(s)):
    for j in range(len(s[0])):
        try:
            if s[i][j:j+4] == "XMAS" or s[i][j:j+4] == "SAMX":
                t += 1
                """
                for k in range(i):print("."*(len(s[0])-1))
                print("."*j + "****" + "."*(len(s[0])-j-5))
                for k in range(len(s)-i-1): print("."*(len(s[0])-1))
                input()"""

        except: pass
        try:
            if s[i][j] + s[i+1][j] + s[i+2][j] + s[i+3][j]== "XMAS" or \
                    s[i][j] + s[i+1][j] + s[i+2][j] + s[i+3][j] == "SAMX":
                t += 1
                """
                for k in range(i): print("."*(len(s[0])-1))
                print("."*j + "*" + "."*(len(s[0])-j-2))
                print("." * j + "*" + "."*(len(s[0])-j-2))
                print("." * j + "*"+"."*(len(s[0])-j-2))
                print("." * j + "*"+"."*(len(s[0])-j-2))
                for k in range(len(s) - i - 4): print("." * (len(s[0]) - 1))
                input()"""
        except: pass
        try:
            if s[i][j] + s[i+1][j+1] + s[i+2][j+2] + s[i+3][j+3] == "XMAS" or \
                    s[i][j] + s[i+1][j+1] + s[i+2][j+2] + s[i+3][j+3] == "SAMX":
                t += 1
                """
                for k in range(i): print("."*(len(s[0])-1))
                print("."*j + "*" + "."*(len(s[0])-j-2))
                print("." * (j+1) + "*"+ "."*(len(s[0])-j-3))
                print("." * (j+2) + "*"+ "."*(len(s[0])-j-4))
                print("." * (j+3) + "*"+ "."*(len(s[0])-j-5))
                for k in range(len(s) - i - 4): print("." * (len(s[0]) - 1))
                input()"""
        except: pass
        try:
            if j-3 >=0:
                if s[i][j] + s[i+1][j-1] + s[i+2][j-2] + s[i+3][j-3] == "XMAS" or \
                        s[i][j] + s[i+1][j-1] + s[i+2][j-2] + s[i+3][j-3] == "SAMX":
                    t += 1
                    """
                    for k in range(i): print("."*(len(s[0])-1))
                    print("."*j + "*"+ "."*(len(s[0])-j-2))
                    print("." * (j-1) + "*"+ "."*(len(s[0])-j-1))
                    print("." * (j-2) + "*"+ "."*(len(s[0])-j))
                    print("." * (j-3) + "*"+ "."*(len(s[0])-j+1))
                    for k in range(len(s) - i - 4): print("." * (len(s[0]) - 1))
                    input()"""
        except: pass

print(t)
t = 0

for i in range(len(s)):
    for j in range(len(s[0])):
        try:
            if (s[i][j] + s[i+1][j+1] + s[i+2][j+2] == "MAS" or s[i][j] + s[i+1][j+1] + s[i+2][j+2] == "SAM") and \
                    (s[i+2][j] + s[i+1][j+1] + s[i][j+2] == "MAS" or s[i+2][j] + s[i+1][j+1] + s[i][j+2] == "SAM") : t+=1
        except: pass

print(t)