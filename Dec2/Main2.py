filename = "Input.txt"

def getHigherDepth(inArr):
    aim = 0
    forward = 0
    depth = 0
    for elem in inArr:
        args = elem.split(" ")
        args[1] = int(args[1])
        forward = forward + args[1] * (args[0] == "forward")
        depth = depth + args[1] * aim * (args[0] == "forward")
        aim = aim + args[1] * (args[0] == "down") - args[1] * (args[0] == "up")
        
    return depth * forward


if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    dayArr = text.split("\n")
    print(getHigherDepth(dayArr))