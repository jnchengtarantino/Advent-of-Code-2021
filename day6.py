# file = open("testinput.txt")
file = open("day6input.txt")
days = 256

lines = file.readlines()
start = lines[0].strip().split(",")
fish = [0,0,0,0,0,0,0,0,0]
for s in start:
    fish[int(s)] += 1

for d in range(days):
    temp = fish[0]
    fish[0] = fish[1]
    fish[1] = fish[2]
    fish[2] = fish[3]
    fish[3] = fish[4]
    fish[4] = fish[5]
    fish[5] = fish[6]
    fish[6] = fish[7]
    fish[7] = fish[8]
    fish[8] = temp
    fish[6] += temp

print(sum(fish))
        
file.close()