import numpy as np
from collections import Counter
# file = open("testinput.txt")
file = open("day14input.txt")

lines = file.readlines()
rules = {}
template = lines[0].strip()
for i in range(2,len(lines)):
    k, _, v = lines[i].strip().split(" ")
    rules[k] = v
pairs = Counter( map(str.__add__,template, template[1:]) )
chars = Counter(template)
for _ in range(40):
    for (a,b), c in pairs.copy().items():
        x = rules[a+b]
        pairs[a+b] -= c
        pairs[a+x] += c
        pairs[x+b] += c
        chars[x] += c
print(max(chars.values())-min(chars.values()))
file.close()