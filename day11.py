import numpy as np

# file = open("testinput.txt")
file = open("day11input.txt")

def step(jellies):
    flash = np.zeros_like(jellies)
    jellies += 1
    temp = np.copy(flash)

    while not np.array_equal(temp,jellies):
        # print(flash)
        temp = np.copy(jellies)
        for i in range(1,len(jellies)-1):
            for j in range(1,len(jellies[0])-1):
                if jellies[i][j] > 9 and flash[i][j] == 0:
                    # print("flash at (" + str(i) +", " + str(j) +")")
                    flash[i][j] = 1
                    jellies[i-1][j-1] += 1
                    jellies[i-1][j] += 1
                    jellies[i-1][j+1] += 1
                    jellies[i][j-1] += 1
                    jellies[i][j+1] += 1
                    jellies[i+1][j-1] += 1
                    jellies[i+1][j] += 1
                    jellies[i+1][j+1] += 1

    for i in range(len(jellies)):
        for j in range(len(jellies[0])):
            if i == 0 or j == 0 or i == len(jellies)-1 or j == len(jellies[0])-1:
                jellies[i][j] = -100
            elif flash[i][j] == 1:
                jellies[i][j] = 0
    if np.sum(flash) == (len(jellies)-2)*(len(jellies[0])-2):
        return True
    else:
        return False

lines = file.readlines()
jellies = []
for line in lines:
    line = [int(c) for c in line.strip()]
    jellies.append(line)
jellies = np.array(jellies)
jellies = np.pad(jellies,1,constant_values=-100)
sum = 0
# print("og")
# print(jellies)
found = -1
current = 0
while found == -1:
    # print("\nafter step " + str(i+1))
    current += 1
    if step(jellies):
        found = current
    print("after step " + str(current))
    # print(jellies)
print(current)
file.close()