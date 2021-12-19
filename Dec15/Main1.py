import numpy as np
filename = "Input.txt"

def getDist(arr,distArr,finished):
    xL = len(arr)
    yL = len(arr[0])
    for x in range(xL):
        for y in range(yL):
            #needsChange = (not(finished[x][y]) and distArr[x][y] != -1)
            pts = {True:[],False:[]}
            pts[x > 0].append((x-1,y))
            pts[x < xL-1].append((x+1,y))
            pts[y > 0].append((x,y-1))
            pts[y < yL-1].append((x,y+1))
            for pt in pts[True]:
                dist = distArr[x][y] + arr[pt[0]][pt[1]]
                change = dist < distArr[pt[0]][pt[1]] or distArr[pt[0]][pt[1]] == -1
                nC = not(change)
                distArr[pt[0]][pt[1]] = (distArr[pt[0]][pt[1]] * nC) + (dist * change)
                finished[pt[0]][pt[1]] = finished[pt[0]][pt[1]] * nC
                
            finished[x][y] = 1
            #If the number has a values
            #Calculate the distance to all of its neighbors
            #For each neighbor:
            #   If distArr[self] + arr[neighbor] < distArr[neighbor]
            #       distArr[neighbor] = distArr[slef] + arr[neighbor]
            #       Mark neighbor as unfinished
            #Once it has done that for each neighbor
            #Mark self as finished
    return (arr,distArr,finished)


if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    numLine = text.split("\n")
    arr = [] #Hold whole array  
    arrL = [] #Hold one line
    for line in numLine:
        arrL = []
        for elem in line:
            arrL.append(int(elem))
        arr.append(arrL)
        
    distArr = np.zeros((len(arr),len(arr[0])))
    distArr -= 1
    distArr[0][0] = arr[0][0]
    finished = np.zeros((len(arr),len(arr[0])))
    
    while((finished==1).sum() != len(arr) * len(arr[0])):
        arr,distArr,finished = getDist(arr,distArr,finished)
        print(distArr)
    print(distArr[len(arr)-1][len(arr[0])-1] - arr[0][0])