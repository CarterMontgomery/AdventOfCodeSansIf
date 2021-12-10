class Board:
    def __init__(self,b):
        self.og = b.copy()
        self.complete = 0
        self.curboard = []
        for x in range(len(self.og)):
            line = []
            for y in range(len(self.og)):
                line.append(self.og[x][y])
            self.curboard.append(line)
    def place(self,num):
        x = -1
        y = -1
        for x1 in range(len(self.curboard)):
            for y1 in range(len(self.curboard[0])):
                
                x += (x==-1)*(self.curboard[x1][y1] == num)*(x1+1)
                y += (y==-1)*(self.curboard[x1][y1] == num)*(y1+1)
        self.curboard[x][y] = self.curboard[x][y] * (x == -1 and y == -1) + (-1 * (x != -1 and y != -1))
        
        return self.didWin()
    def didWin(self):
        ret = 0
        all5 = 0
        #Check cols first
        for col in range(len(self.curboard)):
            sumOG = 0
            all5 = 0
            for elem in range(len(self.curboard[0])):
                all5 += (self.curboard[col][elem] == -1)
                sumOG += self.og[col][elem]
            
            ret += (ret == 0)*(all5== 5) * sumOG
        for row in range(len(self.curboard[0])):
            sumOG = 0
            all5 = 0
            for elem in range(len(self.curboard)):
                all5 += (self.curboard[elem][row] == -1)
                sumOG += self.og[elem][row]
            ret += (ret == 0)*(all5 == 5) * sumOG
        allcomp = self.sumNon()
        allcomp = allcomp * (ret != 0)
        self.complete = (ret != 0)
        return allcomp
    def sumNon(self):
        allcomp = 0
        for row in range(len(self.curboard)):
            for col in range(len(self.curboard[0])):
                allcomp += (self.curboard[row][col] != -1)*self.og[row][col]
        return allcomp
    def printBoard(self):
        print("NEW BOARD:")
        print(self.og)
        print(self.curboard)
    def makeBoard(lines):
        tmpBoard = []
        for line in lines:
            aLine = line.split(" ")
            try:
                while(aLine.index('') != -1):
                    aLine.pop(aLine.index(''))
            except ValueError:
                pass
            for elem in range(len(aLine)):
                aLine[elem] = int(aLine[elem])
            tmpBoard.append(aLine)
        return tmpBoard

filename = "Input.txt"
text = ""
with open(filename) as f:
    text = f.read()
bingoArr = text.split("\n")
cmds=bingoArr[0].split(",")
bingoArr.pop(0)
try:
    while(bingoArr.index('') != -1):
        bingoArr.pop(bingoArr.index(''))
except ValueError:
    pass
boardList = []
line = 0
while (line < len(bingoArr)):
    boardList.append(Board(Board.makeBoard(bingoArr[line:line+5])))
    line = line + 5
choice = 0
found = 0
notDone = True
while (choice < len(cmds) and notDone):
    popList = []
    comp = 0
    found = 0
    for board in range(len(boardList)):
        compl = boardList[board].complete

        found += (not(compl)) * (found == 0) * (int(cmds[choice]) * boardList[board].place(int(cmds[choice])))
        
        comp += boardList[board].complete
    notDone = not(comp == len(boardList))
    
    choice = choice + 1
print(found)