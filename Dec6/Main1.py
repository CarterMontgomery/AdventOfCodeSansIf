import numpy as np
filename = "Input.txt"

def cyclefish(fishdict):
    
    temp8 = fishdict[0]
    for fishtime in range(len(fishdict)-1):
        fishdict[fishtime] = fishdict[fishtime+1]
    fishdict[6] += temp8
    fishdict[8] = temp8
    return fishdict

def getnumfish(fishdict):
    return sum(fishdict.values())

if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    fishes = text.split(",")
    for fish in range(len(fishes)):
        fishes[fish] = int(fishes[fish])
    fishdict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    for fish in fishes:
        fishdict[fish] += 1
    #Decrement all fishes
    #Main1 uses days=80
    days = 80
    for day in range(days):
        cyclefish(fishdict)
    print(getnumfish(fishdict))
    
    