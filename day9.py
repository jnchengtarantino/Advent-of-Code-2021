# file = open("testinput.txt")
file = open("day9input.txt")

import numpy as np

def minima(map):
    mask = np.zeros_like(map)
    for i in range(1,len(map)-1):
        for j in range(1,len(map[0])-1):
            if map[i][j] < map[i-1][j-1] and map[i][j] < map[i-1][j] and map[i][j] < map[i+1][j] and map[i][j] < map[i][j-1] and map[i][j] < map[i][j+1]:
                mask[i][j] = 1
    return mask

def basin(map, x, y, mask, counter = 0):
    counter +=1
    mask[x][y] = 1
    if map[x-1][y] > map[x][y] and mask[x-1][y] == 0 and map[x-1][y] < 9:
        mask = basin(map, x-1, y, mask, counter)
    if map[x+1][y] > map[x][y] and mask[x+1][y] == 0 and map[x+1][y] < 9:
        mask = basin(map, x+1, y, mask, counter)
    if map[x][y-1] > map[x][y] and mask[x][y-1] == 0 and map[x][y-1] < 9:
        mask = basin(map, x, y-1, mask, counter)
    if map[x][y+1] > map[x][y] and mask[x][y+1] == 0 and map[x][y+1] < 9:
        mask = basin(map, x, y+1, mask, counter)
    return mask


lines = file.readlines()
map = []
risk = 0
for line in lines:
    line = [int(n) for n in line.strip()]
    line.insert(0,9)
    line.append(9)
    map.append(line)
map.append([9]*(len(map[0])))
map.insert(0,[9]*(len(map[0])))
map = np.array(map)
mask = minima(map)
basins = []
for i in range(len(mask)):
    for j in range(len(mask[0])):
        if mask[i][j] == 1:
            basin_mask = basin(map,i,j,np.zeros_like(map))
            basins.append(np.sum(basin_mask))
basins.sort()
print(basins[-1]*basins[-2]*basins[-3])
file.close()