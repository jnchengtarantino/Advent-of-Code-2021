import functools
# file = open("testinput.txt")
file = open("day3input.txt")

lines = file.readlines()
count = [0]*(len(lines[0].strip())) 

for i in range(len(lines)):
    for j in range (len(lines[i].strip())):
        if int(lines[i][j]) == 1:
            count[j] += 1
        else:
            count[j] -= 1
gamma = ''
epsilon = ''
for val in count:
    if val > 0:
        gamma +='1'
        epsilon +='0'
    elif val< 0:
        gamma +='0'
        epsilon +='1'
    else:
        gamma +='1'
        epsilon +='1'

oxygen = 0
co2 = 0
crit_o = lines.copy()
crit_c = lines.copy()
for i in range(len(lines[0])):
    bins_o = [x[i] for x in crit_o]
    bins_c = [x[i] for x in crit_c]
    if bins_o.count("1") >= bins_o.count("0"):
        crit_o = [x for x in crit_o if x[i] == "1"]
    else:
        crit_o = [x for x in crit_o if x[i] == "0"]
    if bins_c.count("1") < bins_c.count("0"):
        crit_c = [x for x in crit_c if x[i] == "1"]
    else:
        crit_c = [x for x in crit_c if x[i] == "0"]
    if len(crit_o) == 1:
        oxygen = int(crit_o[0],2)
    if len(crit_c) == 1:
        co2 = int(crit_c[0],2)

print(str(co2*oxygen))
file.close()