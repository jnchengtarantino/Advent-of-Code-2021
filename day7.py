# file = open("testinput.txt")
file = open("day7input.txt")

lines = file.readlines()
start = [int(x) for x in lines[0].strip().split(",")]
maxX = max(start)  

val = min([sum([abs(s-i)*(abs(s-i)+1)/2 for s in start]) for i in range(maxX)])
print(str(val))
file.close()