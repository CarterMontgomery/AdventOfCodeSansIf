filename = "Input.txt"

def step(cur,polys):
    curKeys = cur.keys()
    newcur = {}
    for key in curKeys:
        newcur[key] = 0
    for key in curKeys:
        num = cur[key]
        elem1 = key[0] + polys[key]
        elem2 = polys[key] + key[1]
        newcur[elem1] += num
        newcur[elem2] += num
        
    return newcur




if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    numLine = text.split("\n")
    start = numLine.pop(0)
    #Remove empty line
    numLine.pop(0)
    
    polys = {}
    letters = {}
    cur = {}
    for line in numLine:
        polys[line[0:2]] = line[6]
        cur[line[0:2]] = 0
        letters[line[0]] = 0
    #Initialize cur
    for pair in range(len(start)-1):
        cur[start[pair:pair+2]] += 1
    
    
    steps = 40
    
    for i in range(steps):
        cur = step(cur,polys)
    curKeys = sorted(cur.keys())
    for key in curKeys:
        l1 = key[0]
        letters[l1] += cur[key]
    #Count the last value
    letters[start[len(start)-1]] += 1
    vals = sorted(letters.values())
    print(vals[len(vals)-1]-vals[0])
    
    
