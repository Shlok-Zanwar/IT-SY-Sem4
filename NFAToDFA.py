noOfStates = int(input("Enter number of states     : "))
noOfSymbols = int(input("Enter length of Σ(symbols) : "))


# Making table
def makeTable(disct, rows, col):
    n=len(col)
    print(' '*15, end='') # change this number acc to the len of the largest string in the list rows
    for i in col:
        print('|',i.center(len('q0 q1 q2')+6), end='') # this is the largest string length wise in disct.values
    print(' '*15, end='') # change this number acc to the len of the largest string in the list rows

    print('\n', '-'*45, end='' )
    for i in rows:
        print()
        print(i,end='' )
        print(' ' * (15-len(i)), end='')
        for j in range(n):
            print('|', str(disct[i][j]).center(len('q0 q1 q2') + 5), end=' ')
      # change this number acc to the len of the largest string in the list row


# State name validation
def isItValid(name):
    if len(name.split(" ")) == 1:
        return True
    
    return False


# State names input
nfaStates = []
print("\nEnter name of states.\n")
i = 0
while i < noOfStates:
    temp = input("    Enter name of state " + str(i + 1) + " : ")
    if isItValid(temp):
        if temp != 'qd':
            nfaStates.append(temp)
        else:
            i -= 1
            print("        Invalid state name ('qd' is reserved for dead state)")
    else:
        i -= 1
        print("        Invalid state name")

    i += 1
        
print()


# symbol names input
symbols = []
for i in range(noOfSymbols):
    disp = "    Enter symbol " + str(i + 1) + " : "
    temp = input(disp)
    symbols.append(temp)
# print(symbols)


# making nfa dict
nfaDict = {}
print("\n    Enter states space seperated (Empty Enter if 𝛟)")
for state in range(len(nfaStates)):
    print()
    currState = []
    for symbol in range(len(symbols)):
        print("        Enter out states for '" + symbols[symbol] + "' from state '" + nfaStates[state], end="' : ")
        outStates = input().split(" ")
        if(outStates[0] == ''):
            outStates.pop()
        currState.append(outStates)
        # print(outStates)
    nfaDict[nfaStates[state]] = currState



print("\n\nNFA Table :-")
makeTable(nfaDict, nfaStates, symbols)
print("\n")

dfaStates = []
dfaDict = {}
prevDfaStatesLen = len(dfaStates)
deadState = ["qd"]*len(symbols) 
deadStatePresent = False

# Creating initial states (only single letter ones)
for state in range(len(nfaStates)):

    stateName = nfaStates[state]
    if stateName not in dfaStates:
        dfaDict[stateName] = None
        dfaStates.append(stateName)
        
    currState = nfaDict.get(stateName)
    newDfaRow = []
    for i in range(len(symbols)):

        if len(currState[i]) == 0:
            deadStatePresent = True
            newDfaRow.append('qd')
            continue

        if len(currState[i]) == 1:
            nextState = currState[i][0]
        else:
            nextState = " ".join(currState[i])

        if nextState not in dfaStates:
            dfaStates.append(nextState)
            dfaDict[nextState] = None

        newDfaRow.append(nextState)

    dfaDict[stateName] = newDfaRow



def areAllDone(myDict, myStates):
    for state in myStates:
        if myDict.get(state) == None:
            return False
    return True


# Creating double states waale
while True:
    if(areAllDone(dfaDict, dfaStates)):
        break
    
    for state in dfaStates:
        if dfaDict.get(state) == None:
            myParentStates = state.split(" ")

            finalStateAns = []
            for i in range(len(symbols)):
                myAns = []
                for parentState in myParentStates:
                    tempSplit = dfaDict.get(parentState)[i].split(" ")

                    if(tempSplit[0] != ''):
                        for symbol in tempSplit:
                            if symbol not in myAns:
                                if symbol != "qd":
                                    myAns.append(symbol)

                newState = " ".join(myAns)
                if newState not in dfaStates:
                    dfaStates.append(newState)
                    dfaDict[newState] = None 

                finalStateAns.append(newState)
            dfaDict[state] = finalStateAns


# deleting useless states
def isDeadStatePresent(myDict, myStates):
    for state in myStates:
        data = myDict.get(state)
        if 'qd' in data:
            return True
    return False


allDeadPresent = True
while True:
    if not isDeadStatePresent(dfaDict, dfaStates):
        break

    if not allDeadPresent:
        break

    allDeadPresent = False
    for state in dfaStates:
        currrCount = 0
        data = dfaDict.get(state)
        for one in data:
            if one == 'qd':
                currrCount += 1

        if currrCount == len(symbols):
            allDeadPresent = True
            dfaDict.pop(state)
            dfaStates.remove(state)

            for stateAgain in dfaStates:
                newData = dfaDict.get(stateAgain)
                for i in range(len(symbols)):
                    if newData[i] == state:
                        dfaDict[stateAgain][i] = "qd"

        
        continue


if isDeadStatePresent(dfaDict, dfaStates):
    dfaDict['qd'] = deadState
    dfaStates.append('qd')

# print(dfaStates)
# print(dfaDict)

print("\n\nDFA Table :-")
makeTable(dfaDict, dfaStates, symbols)

