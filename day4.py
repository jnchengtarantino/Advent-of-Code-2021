import numpy as np
# file = open("testinput.txt")
file = open("day4input.txt")
def check(board):
    board = np.array(board)
    for row in board:
        if sum(row) == 5:
            return True
    t = board.transpose()
    for column in t:
        if sum(column) == 5:
            return True
    return False

def checkAll(marks,boards):
    winners=[]
    for i in range(len(marks)):
        if check(marks[i]):
            winners.append(i)
    return(winners)

def score(board, marks, lastN):
    s = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if marks[i][j] == 0:
                s += board[i][j]
    s *= lastN
    return s

def remove(boards, marks, winners):
    winners.reverse()
    for i in winners:
        if len(boards) > 1:
            del marks[i]
            del boards[i]
        else:
            return True
    return False

lines = file.readlines()
nums = [int(num) for num in lines[0].strip().split(",")]
boards = []
tempBoard = []
marks = []
tempMark =[]
for i in range(2,len(lines)):
    if lines[i].strip() == "":
        boards.append(tempBoard)
        tempBoard =[]
        marks.append(tempMark)
        tempMark = []
    else:
        line = lines[i].strip().split(" ")
        tempBoard.append([int(n) for n in line if n != ''])     
        tempMark.append([0,0,0,0,0]) 
boards.append(tempBoard)
marks.append(tempMark)
winners = []
lastN = None
done = False
for n in nums:
    print("drew " +str(n))
    for b in range(len(boards)):
        for x in range(len(boards[0])):
            for y in range(len(boards[0][0])):
                if boards[b][x][y] == n:
                    marks[b][x][y] = 1
                    print("marking b " + str(b) + " x " +str(x)+" y "+str(y))
    winners = checkAll(marks,boards)
    done = remove(boards,marks,winners)
    if (done):
        lastN = n
        break

print(score(boards[0],marks[0],lastN))
file.close()