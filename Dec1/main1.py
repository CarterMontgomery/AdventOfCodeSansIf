filename = "Input.txt"

def getHigherDepth(inArr):
    higher = 0
    for elem in range(len(inArr)-1):
        higher = higher + 1*(int(inArr[elem+1]) > int(inArr[elem]))
    return higher

if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    dayArr = text.split("\n")
    print(getHigherDepth(dayArr))