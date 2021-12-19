filename = "Input.txt"

def step(cur,polys):
    new = ""
    for index in range(len(cur)-1):
        new += cur[index]
        new += polys[cur[index]+cur[index+1]]
    new += cur[len(cur)-1]
    return new



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
    for line in numLine:
        polys[line[0:2]] = line[6]
        letters[line[0]] = 0
    
    steps = 10
    cur = start
    #Naive solution
    for i in range(steps):
        cur = step(cur,polys)
    for letter in cur:
        letters[letter] += 1
    vals = sorted(letters.values())
    print(vals[len(vals)-1]-vals[0])
    
