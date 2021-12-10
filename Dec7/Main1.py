import numpy as np
filename = "Input.txt"

if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    crabI = text.split(",")
    for crab in range(len(crabI)):
        crabI[crab] = int(crabI[crab])
    crabdict = {}
    for crab in crabI:
        crabdict[crab] = crabI.count(crab)
    lowFuel = 1000000
    lowFuelI = -1
    for i in range(max(crabI)):
        curFuel = 0
        for key in crabdict.keys():
            curFuel += (abs(key - (i+1)) * crabdict[key])
        lowFuelI = (i+1) * (curFuel < lowFuel) + (lowFuelI * (curFuel >= lowFuel))
        lowFuel = curFuel * (curFuel < lowFuel) + (lowFuel * (curFuel >= lowFuel))
    print(lowFuelI,lowFuel)
        
    