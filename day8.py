# file = open("testinput.txt")
file = open("day8input.txt")

lines = file.readlines()
sum = 0
for line in lines:
    p, o = line.strip().split("|")
    p = p.strip().split(" ")
    p = ["".join(sorted(pat.strip())) for pat in p]
    o = o.strip().split(" ")
    o = ["".join(sorted(out.strip())) for out in o]
    ind = [""] * 10
    for pat in p:
        if len(pat) == 2:
            ind[1] = pat
        elif len(pat) == 3:
            ind[7] = pat
        elif len(pat) == 4:
            ind[4] = pat
        elif len(pat) == 7:
            ind[8] = pat
    
    diff = [c for c in ind[4] if c not in ind[1]]
    one = [c for c in ind[1]]
    for pat in p:
        if len(pat) == 5:
            if diff[0] in pat and diff[1] in pat:
                ind[5] = pat
            elif one[0] in pat and one[1] in pat:
                ind[3] = pat
            else:
                ind[2] = pat
        elif len(pat) == 6:
            if diff[0] not in pat or diff[1] not in pat:
                ind[0] = pat
            elif one[0] in pat and one[1] in pat:
                ind[9] = pat
            else:
                ind[6] = pat
    
    sum += ind.index(o[0]) * (10**3) + ind.index(o[1]) * (10**2) + ind.index(o[2]) * 10 + ind.index(o[3])

print(str(sum))
file.close()