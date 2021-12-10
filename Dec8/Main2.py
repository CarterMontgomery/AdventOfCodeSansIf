import numpy as np
filename = "Input.txt"


def parseLine(line):

    spl = line.split("|")
    inputR = spl[0].split(" ")
    inputR.pop()
    outputR = spl[1].split(" ")
    outputR.pop(0)
    inputDict = {}
    for v in inputR:
        inputDict["".join(sorted(v))] = -1
    inputDict = parseNums(inputDict)
    outArr = []
    for v in outputR:
        outArr.append(inputDict["".join(sorted(v))])
    return outArr

def parseNums(inDict):
    keys = inDict.keys()
    #Find the 1, 7, 8, 4.
    #Dict to hold possible positions
    pos = np.asarray(["a", "b", "c", "d", "e", "f", "g"])
    #  0
    #1   2
    #  3
    #4   5 
    #  6
    posD = {0:"",1:"",2:"",3:"",4:"",5:"",6:""}
    #Letters holds the count of all letters we can get. 9, 4, and 6 are unique letter counts.
    letters = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0}
    for k in keys:
        for l in letters.keys():
            letters[l] += l in k
        #Get Obvious
        inDict[k] += (1+1) * (len(k) == 2)
        inDict[k] += (1+4) * (len(k) == 4)
        inDict[k] += (1+7) * (len(k) == 3)
        inDict[k] += (1+8) * (len(k) == 7)
    #Use letters to get all we can.
    keyL = list(letters.keys())
    valL = list(letters.values())
    posD[5] = keyL[valL.index(9)]
    posD[4] = keyL[valL.index(4)]
    posD[1] = keyL[valL.index(6)]
    #Now that we have 1 and 7, we find index 0.
    keyP = list(inDict.keys())
    valP = list(inDict.values())
    pos1 = keyP[valP.index(1)]
    pos7 = keyP[valP.index(7)]
    temp = sorted(pos7)
    temp.pop(temp.index(pos1[0]))
    temp.pop(temp.index(pos1[1]))
    posD[0] = temp[0]
    leftover = sorted(pos1)
    leftover.pop(pos1.index(posD[5]))
    posD[2] = leftover[0]
    #We now need 3 and 6 left in posD
    pos4 = keyP[valP.index(4)]
    #4 can get 3.
    temp = sorted(pos4)
    temp.pop(temp.index(posD[1]))
    temp.pop(temp.index(posD[2]))
    temp.pop(temp.index(posD[5]))
    posD[3] = temp[0]
    pos8 = keyP[valP.index(8)]
    temp = sorted(pos8)
    temp.pop(temp.index(posD[0]))
    temp.pop(temp.index(posD[1]))
    temp.pop(temp.index(posD[2]))
    temp.pop(temp.index(posD[3]))
    temp.pop(temp.index(posD[4]))
    temp.pop(temp.index(posD[5]))
    posD[6] = temp[0]
    #We already have 1, 4, 7, 8
    output = {}
    output[0] = reassemble(posD,[0,1,2,4,5,6])
    output[1] = reassemble(posD,[2,5])
    output[2] = reassemble(posD,[0,2,3,4,6])
    output[3] = reassemble(posD,[0,2,3,5,6])
    output[4] = reassemble(posD,[1,2,3,5])
    output[5] = reassemble(posD,[0,1,3,5,6])
    output[6] = reassemble(posD,[0,1,3,4,5,6])
    output[7] = reassemble(posD,[0,2,5])
    output[8] = reassemble(posD,[0,1,2,3,4,5,6])
    output[9] = reassemble(posD,[0,1,2,3,5,6])
    outK = list(output.keys())
    outV = list(output.values())
    for key in inDict.keys():
        
        inDict[key] = outK[outV.index(key)]
    return inDict
    
def reassemble(posD,real):
    ret = ""
    for v in real:
        ret += posD[v]
    return "".join(sorted(ret))
    

if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    numLine = text.split("\n")
    results = {-1:0,0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0} 
    sumN = 0
    for line in numLine:
        output = parseLine(line)
        temp = 0
        for v in output:
            temp = temp * 10 + v
        sumN += temp
        for output in parseLine(line):
            results[output] += 1
    print("PART 2: ",sumN)
    