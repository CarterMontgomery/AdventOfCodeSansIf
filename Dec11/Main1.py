import numpy as np
filename = "Input.txt"

def step_oct(octopus):
    octopus += 1
    needsFlash = {True:[],False:[]}
    for x in range(len(octopus)):
        for y in range(len(octopus[x])):
            needsFlash[octopus[x][y] > 9].append((x,y))
            octopus[x][y] = octopus[x][y] * (octopus[x][y] <= 9)
    flashes = 0
    for octFlash in needsFlash[True]:
        flash(octopus,octFlash[0],octFlash[1],True)
    return (octopus == 0).sum()
    

def flash(octopus,x,y,start):
    
    #print("Flashing ",octopus[x][y],x,y,start)
    needsToFlash = octopus[x][y] != 0 or start
    #subflashes = 1*(start or octopus[x][y] != 0)
    octopus[x][y] = 0

    goodBad = {"Coords":{True:[],False:[]},"Flashed":{True:[],False:[]},"Run":{True:[],False:[]}}
    xGoodLeft = (x > 0)  and needsToFlash
    xGoodRight = (x < len(octopus)-1) and needsToFlash
    yGoodTop = (y > 0) and needsToFlash
    yGoodBot = (y < len(octopus[0])-1) and needsToFlash
    # (x-1,y-1) (x,y-1) (x+1,y-1)  (xGoodLeft and yGoodTop) (yGoodTop) (xGoodRight and yGoodTop)
    # (x-1, y)  (x,y)   (x+1,y)
    # (x-1,y+1) (x,y+1) (x+1,y+1)    
    goodBad["Coords"][(xGoodLeft and yGoodTop)].append((x-1,y-1))
    goodBad["Coords"][(yGoodTop)].append((x,y-1))
    goodBad["Coords"][(xGoodRight and yGoodTop)].append((x+1,y-1))
    goodBad["Coords"][(xGoodLeft)].append((x-1,y))
    goodBad["Coords"][(xGoodRight)].append((x+1,y))
    goodBad["Coords"][(xGoodLeft and yGoodBot)].append((x-1,y+1))
    goodBad["Coords"][(yGoodBot)].append((x,y+1))
    goodBad["Coords"][(xGoodRight and yGoodBot)].append((x+1,y+1))
    for coord in goodBad["Coords"][True]:
        goodBad["Flashed"][(octopus[coord[0]][coord[1]] != 0)].append(coord)
    for notFlashed in goodBad["Flashed"][True]:
        octopus[notFlashed[0]][notFlashed[1]] += 1
        goodBad["Run"][checkFlash(octopus,notFlashed[0],notFlashed[1])].append(notFlashed)
    for needsToFlash in goodBad["Run"][True]:
        flash(octopus,needsToFlash[0],needsToFlash[1],False)
    #return subflashes
def checkFlash(octopus,x,y):
    return octopus[x][y] > 9

if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    numLine = text.split("\n")
    bigMatrix = []
    
    for line in numLine:
        tL = []
        for num in line:
            tL.append(int(num))
        bigMatrix.append(tL)
    octopus = np.asarray(bigMatrix)
    stepflashes = 0
    for num in range(100):
        stepflashes += (step_oct(octopus))
    print(stepflashes)