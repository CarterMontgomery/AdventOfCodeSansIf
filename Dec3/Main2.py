filename = "Input.txt"

def getCommonBit(inArr,pos):
    arr = 0
    
    for elem in range(len(inArr)):
        arr += int(inArr[elem][pos])
    avg = len(inArr)
    high = 0
    high = arr/avg >= .5
    return high

def loopDown(inArr, srch):
    curArr = inArr
    
    pos = 0
    while (pos < len(inArr[0]) and len(curArr) > 1):
        cb = getCommonBit(curArr,pos)
        cb = not(cb ^ srch)
        tmpArr = []
        for elem in curArr:
            if (int(elem[pos]) == cb):
                tmpArr.append(elem)
        curArr = tmpArr
        pos = pos + 1
    return curArr
        

def toDec(val):
    rev = val[::-1]
    result = 0
    pow2 = 1
    for elem in range(len(rev)):
        result = result + pow2*int(rev[elem])
        pow2 = pow2 * 2
    return result


#If srch = 1 and cb = 1 cb = 1
#If srch = 1 and cb = 0 cb = 0
#If srch = 0 and cb = 1 cb = 0
#If srch = 0 and cb = 0 cb = 1
#Process:
#Take array dayArr
#While the array has more than one val, loop:
#Get most common bit at position
#Make new array with vals at the position
#Increment array


if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    dayArr = text.split("\n")
    high, low = loopDown(dayArr,1)[0],loopDown(dayArr,0)[0]
    print(high,low)
    high = toDec(high)
    low = toDec(low)
    print(high*low)