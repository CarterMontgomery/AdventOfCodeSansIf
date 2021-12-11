import numpy as np
filename = "Input.txt"
opposite = {'[':']','(':')','{':'}','<':'>',']':'[',')':'(','}':'{','>':'<'}
closes = [')',']','}','>']
opens = ['(','[','{','<']
"""
#Make a dictionary of each possible input
#Make an array of all opening ones
#opposite = {'[':']','(':')','{','}','<':'>',']':'[',')':'(','}':'{','>':'<'}
#closes = [')',']','}','>']
#<<([])>{}>
#'<': [0, 1]
#'(': [2]
#'[': [3]
#']': [4]
#
#True: [0,1,2,3]
#False: 
#When encountering a close, get the last value in True by popping it
#If it equals a value in the corresponding array, we are good. 
#onChar = ']'
#dict[onChar].append(index)
#close = onChar in closes
#dict[not(close)].append(index)
#dict[False].append(-1)
#val = dict[close].pop()
#opp = opposite[onChar]
#validate = index * ((val in dict[opp] or val in closes) and not validate)
"""

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

if __name__ == "__main__":
    text = ""
    with open(filename) as f:
        text = f.read()
    numLine = text.split("\n")
    summ = 0
    for line in numLine:
        summ +=(getFirstWrong(line))
    print( summ)
    