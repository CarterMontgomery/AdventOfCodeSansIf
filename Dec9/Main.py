import numpy as np
filename = "TestInput.txt"


def getLowPoints(bm):
    riskVal = 0
    #Get the middle low points
    
    for x in (range(len(bm))):
        for y in range(len(bm[x])):
            v = bm[x][y]
            found = ((v < bm[x-1][y] or x==0) and (v < bm[(x+1) % len(bm)][y] or x==len(bm)-1) 
                    and (v < bm[x][y-1] or y==0) and (v < bm[x][(y+1) % len(bm[0])] or y == len(bm[0])-1))
            riskVal += (v+1) * found
    
    return riskVal

if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    numLine = text.split("\n")
    bigMatrix = []
    tL = []
    for line in numLine:
        tL = []
        for num in line:
            tL.append(int(num))
        bigMatrix.append(tL)
    #print(bigMatrix)
    riskVal = getLowPoints(bigMatrix)
    print(riskVal)