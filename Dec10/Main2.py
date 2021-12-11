filename = "Input.txt"
opposite = {'[':']','(':')','{':'}','<':'>',']':'[',')':'(','}':'{','>':'<'}
closes = [')',']','}','>']
opens = ['(','[','{','<']


def getFirstWrong(line):
    indexDict = {'(':[],'[':[],'{':[],'<':[],')':[],']':[],'}':[],'>':[],True:[],False:[]}
    vals = {')':3,']':57,'}':1197,'>':25137,'.':0}
    """
    ): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
"""
    validate = False
    ret = -1
    for index in range(len(line)):
        onChar = line[index]
        indexDict[onChar].append(index)
        close = onChar in closes
        indexDict[not(close)].append(index)
        indexDict[False].append(-1)
        val = indexDict[close].pop()
        opp = opposite[onChar]
        validate += ((not(val in indexDict[opp]) and (onChar in closes)) and not validate)
        ret += ((index+1) * validate * (ret == -1))
    line+=(".")
    
    return vals[line[ret]]

def iteratePartTwo(line):
    indexDict = {'(':[],'[':[],'{':[],'<':[],')':[],']':[],'}':[],'>':[],True:[],False:[]}
    vals = {')':1,']':2,'}':3,'>':4}
    for index in range(len(line)):
        onChar = line[index]
        indexDict[onChar].append(index)
        close = onChar in closes
        indexDict[not(close)].append(index)
        indexDict[False].append(-1)
        val = indexDict[close].pop()
    result = ""
    for item in indexDict[True][::-1]:
        result += (opposite[line[item]])
    ret = 0
    for letter in result:
        ret = (ret * 5) + vals[letter]
    return ret
if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    numLine = text.split("\n")
    summ = 0
    part1 = {True:[],False:[]}
    for line in numLine:
        part =(getFirstWrong(line))
        part1[part==0].append(line)
        summ+=part
    print( summ)
    part2 = []
    for line in part1[True]:
        part2.append(iteratePartTwo(line))
    print(sorted(part2)[int(len(part2)/2)])
    