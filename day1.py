file = open("day1input.txt")
lines = file.readlines()

increase = 0
for i in range(3,len(lines)):
    if ( int(lines[i]) + int(lines[i-1]) + int(lines[i-2]) )> ( int(lines[i-1]) + int(lines[i-2]) + int(lines[i-3]) ):
        increase +=1

print(increase)
file.close()