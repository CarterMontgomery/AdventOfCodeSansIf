filename = "Input.txt"

def getBits(inArr):
    arr = []
    high = []
    low = []
    for zero in range(len(inArr[0])):
        arr.append(0)
        high.append(0)
        low.append(0)
    for elem in range(len(inArr)):
        for subA in range(len(inArr[elem])):
            
            arr[subA] += int(inArr[elem][subA])
    
    avg = len(inArr)
    for i in range(len(inArr[0])):
        high[i] = arr[i]/avg > .5
        low[i] = not(high[i])
    return high, low

def toDec(val):
    rev = val[::-1]
    result = 0
    pow2 = 1
    for elem in range(len(rev)):
        result = result + pow2*rev[elem]
        pow2 = pow2 * 2
    return result


if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    dayArr = text.split("\n")
    high, low = (getBits(dayArr))
    high = toDec(high)
    low = toDec(low)
    print(high*low)