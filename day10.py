from statistics import median
# file = open("testinput.txt")
file = open("day10input.txt")

lines = file.readlines()
score = []
for line in lines:
    line = line.strip()
    done = False
    while not done:
        temp = line.replace('[]','').replace('()','').replace('{}','').replace('<>','')
        if line == temp:
            done = True
        line = temp
    if ')' not in line and ']' not in line and '}' not in line and '>' not in line:
        line = line[::-1]
        tempscore = 0
        for c in line:
            if c =='(':
                tempscore = (tempscore*5) +1
            elif c =='[':
                tempscore = (tempscore*5) +2
            elif c =='{':
                tempscore = (tempscore*5) +3
            elif c =='<':
                tempscore = (tempscore*5) +4
        score.append( tempscore )
    
print(median(score))   
file.close()