filename = "Input.txt"


def getUniquePts(elements,numLine):
    for line in numLine:
        elems = line.split("-")
        elements[elems[0]] = []
        elements[elems[1]] = []
def establishLinks(elements,numLine):
    for line in numLine:
        elems = line.split("-")
        elements[elems[0]].append(elems[1])
        elements[elems[1]].append(elems[0])

def getPaths(elements):
    return step("start","start",elements)
#take one step down the path, then split for each valid step 
def step(path,loc,elements):
    #ret = 0
    validPaths = {True:[],False:[]}
    ret = loc == "end"
    arrpath = path.split(",")
    for option in elements[loc]:
        valid = (loc != "end") and (loc != "start" or len(arrpath) == 1)
        valid = valid and (path.find(option) == -1 or option.isupper())
        validPaths[valid].append(option)
    for validPath in validPaths[True]:
        newpath = path +"," +validPath
        ret += step(newpath,validPath,elements)
    return ret

if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    numLine = text.split("\n")
    elements = {"start":[],"end":[]}
    getUniquePts(elements,numLine)
    establishLinks(elements,numLine)
    
    validPaths = getPaths(elements)
    print(validPaths)