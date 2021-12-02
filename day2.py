file = open("day2input.txt")
lines = file.readlines()

hor = 0
depth = 0
aim = 0
for i in range(len(lines)):
    cmd, val = lines[i].split(" ")
    val = int(val)
    
    if cmd == "forward":
        hor += val
        depth += aim*val
    elif cmd == "down":
        aim += val
    else:
        aim -= val

print(str(hor*depth))
        
file.close()