import numpy
# file = open("testinput.txt")
file = open("day5input.txt")

lines = file.readlines()
vents = []
maxX = 0
maxY = 0
for line in lines:
    temp = line.strip().split(" ")
    x1, y1 = temp[0].split(",")
    x2, y2 = temp[2].split(",")
    tempDict = {
        "x1": int(x1),
        "x2": int(x2),
        "y1": int(y1),
        "y2": int(y2)
    }
    maxX = max(maxX,int(x1),int(x2))
    maxY = max(maxY,int(y1),int(y2))
    vents.append(tempDict)        

m = [[0 for j in range(maxY+1)] for i in range(maxX+1)]
for vent in vents:
    if vent["x1"] == vent["x2"]:
        if vent["y1"] < vent["y2"]:
            for j in range(vent["y1"], vent["y2"]+1):
                m[vent["x1"]][j] += 1
        else:
            for j in range(vent["y2"], vent["y1"]+1):
                m[vent["x1"]][j] += 1
    elif vent["y1"] == vent["y2"]:
        if vent["x1"] < vent["x2"]:
            for i in range(vent["x1"], vent["x2"]+1):
                m[i][vent["y1"]] += 1
        else:
            for i in range(vent["x2"], vent["x1"]+1):
                m[i][vent["y1"]] += 1
    else:
        xpos = []
        ypos = []
        print(vent)
        if vent["x1"]<vent["x2"]:
            xpos = [(vent["x1"] + i) for i in range(vent["x2"]-vent["x1"]+1)]
        else:
            xpos = [(vent["x1"] - i) for i in range(vent["x1"]-vent["x2"]+1)]
        if vent["y1"]<vent["y2"]:
            ypos = [(vent["y1"] + i) for i in range(vent["y2"]-vent["y1"]+1)]
        else:
            ypos = [(vent["y1"] - i) for i in range(vent["y1"]-vent["y2"]+1)]
        print("xpos")
        print(xpos)
        print("ypos")
        print(ypos)
        for i in range(len(xpos)):
            m[xpos[i]][ypos[i]] += 1

count = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] > 1:
            count += 1
print(numpy.transpose(m))
print(str(count))
file.close()