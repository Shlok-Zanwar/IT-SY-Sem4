myList = list(map(int, input("Enter the integers (space separated) : ").split()))
myReverseList = []
total = len(myList) - 1

while total >= 0:
    myReverseList.append(myList[total])
    total -= 1

sumList = []
for i in range(len(myList)):
    sumList.append(myList[i] + myReverseList[i])

print("Input   = " + str(myList))
print("Reverse = " + str(myReverseList))
print("Sum     = " + str(sumList))
