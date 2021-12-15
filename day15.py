import numpy as np
from collections import Counter
# file = open("testinput.txt")
file = open("day15input.txt")

lines = file.readlines()
cavePattern = np.array([[int(n) for n in line.strip()] for line in lines]) 
rowPattern = np.copy(cavePattern)
for j in range(1,5):
    cavePattern += 1
    cavePattern[cavePattern == 10] = 1
    rowPattern = np.concatenate((rowPattern,cavePattern),axis=1)

cave = np.copy(rowPattern)
for i in range(1,5):
    rowPattern += 1
    rowPattern[rowPattern==10] = 1
    cave = np.concatenate((cave,rowPattern),axis=0)
path = np.full(cave.shape,100000000)
path[0][0] = 0
while np.any(path ==100000000):
    for i in range(len(path)):
        for j in range(len(path[0])):
            if i >= 0:
                upper = path[i-1][j] + cave[i][j]
            else:
                upper = 100000000 + cave[i][j]
            if i < len(path)-1:
                lower = path[i+1][j] + cave[i][j]
            else:
                lower = 100000000 + cave[i][j]
            if j >= 0:
                left = path[i][j-1] + cave[i][j]
            else:
                left = 100000000 + cave[i][j]
            if j < len(path[0])-1:
                right = path[i][j+1] + cave[i][j]
            else:
                right = 100000000 + cave[i][j]
            path[i][j] = min(path[i][j], upper, lower, right, left)
print(path[len(path)-1][len(path[0])-1])       
file.close()
