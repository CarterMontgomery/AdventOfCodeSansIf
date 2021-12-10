filename = "Input.txt"

def getHigherDepth(inArr):
    higher = 0
    for elem in range(len(inArr)-3):
        A = int(inArr[elem+0])
        B = int(inArr[elem+3])
        
        higher = higher + 1*(A < B)
    return higher



if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    dayArr = text.split("\n")
    print(getHigherDepth(dayArr))