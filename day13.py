import numpy as np
from numpy.core.numeric import zeros_like
# file = open("testinput.txt")
file = open("day13input.txt")

page = np.array([[0]])
instructions = []

lines = file.readlines()
for line in lines:
    # print(line)
    line = line.strip().split(" ")
    if line[0] == 'fold':
        instructions.append(line[2])
    elif line[0] != '':
        x, y = line[0].split(",")
        x = int(x)
        y = int(y)
        if len(page) < y+1:
            page = np.pad(page,( (0, y+1-len(page)),(0,0) ), constant_values=0 )
        if len(page[0]) < x+1:
            page = np.pad(page,((0, 0),(0,x+1-len(page[0]))), constant_values=0 )
    page[y][x] = 1

for instr in instructions:
    a,n = instr.split('=')
    a = 0 if a == 'y' else 1
    n = int(n)
    p1,trash,p2 = np.split(page,[n,n+1],axis=a)
    if a == 0:
        if len(p1) > len(p2):
            p2 = np.pad(page,( (0, len(p1) - len(p2)),(0,0) ), constant_values=0 )
            pass
        elif len(p2) > len(p1):
            p1 = np.pad(page,( (0, len(p2) - len(p1)),(0,0) ), constant_values=0 )
            pass
    else:
        if len(p1[0]) > len(p2[0]):
            p2 = np.pad(page,( (0, len(p1[0]) - len(p2[0])),(0,0) ), constant_values=0 )
            pass
        elif len(p2[0]) > len(p1[0]):
            p1 = np.pad(page,( (0, len(p2[0]) - len(p1[0])),(0,0) ), constant_values=0 )
            pass
    p2 = np.flip(p2,a)
    page = p1 | p2
for x in page:
    print(str(x).replace(" ","").replace("\n","").replace("0"," ").replace("1","#"))
file.close()