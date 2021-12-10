import numpy as np
filename = "Input.txt"


def getBasins(bm):
    riskVal = 0
    #Get the middle low points
    lpA = np.zeros((len(bm),len(bm[0])))
    count = 0
    nines = 0
    for x in (range(len(bm))):
        for y in range(len(bm[x])):
            v = bm[x][y]
            found = ((v < bm[x-1][y] or x==0) and (v < bm[(x+1) % len(bm)][y] or x==len(bm)-1) 
                    and (v < bm[x][y-1] or y==0) and (v < bm[x][(y+1) % len(bm[0])] or y == len(bm[0])-1))
            nines += v==9
            count += found
            riskVal += (v+1) * found
            lpA[x][y] += count * found
    
    while ((lpA==0).sum() != nines):
        for x in (range(len(bm))):
            for y in range(len(bm[x])):
                #If bigger than a neighbor and that neighbor is part of a low region
                #Assign self to that low region
                v = bm[x][y]
                before = lpA[x][y]
                changeable = v != 9 and (lpA[x][y] == 0)
                #Check above
            
                lpA[x][y] += (lpA[x-1][y]) * (changeable and (x!=0) and (lpA[x-1][y] != 0 and v > bm[x-1][y]))
                changeable = v != 9 and (lpA[x][y] == 0)

                #Check below
                lpA[x][y] += (lpA[(x+1) % len(bm)][y]) * (changeable and (x!=len(bm)-1) and (lpA[(x+1) % len(bm)][y] != 0 and v > bm[(x+1) % len(bm)][y]))
                changeable = v != 9 and (lpA[x][y] == 0)

                #Check left
                lpA[x][y] += (lpA[x][y-1]) * (changeable and (y!=0) and (lpA[x][y-1] != 0 and v > bm[x][y-1]))
                changeable = v != 9 and (lpA[x][y] == 0)

                #check right
                lpA[x][y] += (lpA[x][(y+1) % len(bm[x])]) * (changeable and (y!= len(bm[x])-1 and (lpA[x][(y+1)%len(bm[x])] != 0 and v > bm[x][(y+1) % len(bm[x])]))) 
    return lpA,count

def getBasinSize(lpA,count):
    basins = {}
    for elem in range(count):
        basins[elem+1] = (lpA==elem+1).sum()
    return basins,count


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
    basins,count = getBasins(bigMatrix)
    basinDict,count = getBasinSize(basins,count)
    sortedvals = sorted(list(basinDict.values()))[::-1]
    mult = sortedvals[0]*sortedvals[1]*sortedvals[2]
    print(mult)