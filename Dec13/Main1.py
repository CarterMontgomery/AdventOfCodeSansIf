filename = "Input.txt"
def foldA(point,direction,value):
    #print(point,direction,value)
    dire = 1 * direction
    #Point has an x value, and a y value
    #Direction will be 0 if x, 1 if y.
    #Point in form [x,y]
    needsFold = point[dire] > value
    #Now the point is on the other side of the fold
    #Need to check if the point will still exist
    newpoint = point[dire] - value
    stillOn = newpoint <= value
    point[dire] = (point[dire]*(not(needsFold))) + ((value-newpoint) * (needsFold))
    point[dire] = ((point[dire]+1) * stillOn) - 1
    
def performFold(points,foldD):
    x = not("x" in fold1)
    foldval = int(fold1[2:])
    #print(pts)
    for pointI in range(len(pts)):
        foldA(pts[pointI],x,foldval)
    #Remove duplicates
    duplicates = {}
    for point in pts:
        duplicates[str(point)] = 0
    newpts = []
    for point in duplicates.keys():
        x = point[1:point.find(",")]
        y = point[point.find(",")+1:point.find("]")]
        newpts.append([int(x),int(y)])
    return newpts

if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    numLine = text.split("\n")
    
    inputs = {"points":[],"folds":[]}
    for line in numLine:
        inputs["points"].append(line)
    done = False
    fold = inputs["points"].pop()
    while (fold != ""):
        inputs["folds"].append(fold)
        fold = inputs["points"].pop()
    inputs["folds"] = inputs["folds"][::-1]
    pts = []
    for point in inputs["points"]:
        coords = point.split(",")
        pts.append([int(coords[0]),int(coords[1])])
    #Part 1 is just one fold
    
    fold1 = inputs["folds"][0][11:]
    pts = performFold(pts,fold1)
    
    #print(pts)
    print(len(pts))
