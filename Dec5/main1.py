import numpy as np
filename = "Input.txt"

maxN = 0
def parseInput(pts):
    global maxN
    sides = pts.split("->")
    left = sides[0].split(",")
    right = sides[1].split(",")
    left.extend(right)
    for elem in range(len(left)):
        left[elem] = int(left[elem])
    maxN = maxN * (maxN > max(left)) + max(left) * (maxN <= max(left))
    return left
    
def loop(lines,board):
    for line in lines:
        highX = max(line[0],line[2])
        highY = max(line[1],line[3])
        lowX = min(line[0],line[2])
        lowY = min(line[1],line[3])
        direction = 1*(lowX==highX)+2*(lowY==highY)
        #Dir = 0 for diag, 1 for x, 2 for y, 3 for just a point
        numSteps = (highY-lowY)*(direction < 2) + (highX-lowX)*(direction == 2)
        curX = lowX
        curY = lowY
        for step in range(numSteps+1):
            board[curX][curY] += (direction != 0)
            curX += 1 * (direction == 0 or direction == 2)
            curY += 1 * (direction < 2)
    return board
def parseBig(board):
    ret = 0
    for x in board:
        for y in x:
            ret += y > 1
    return ret


if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    lines = text.split("\n")
    newLines = []
    for line in lines:
        newLines.append(parseInput(line))
    board = np.zeros((maxN+1,maxN+1))
    board = loop(newLines,board)
    print(parseBig(board))