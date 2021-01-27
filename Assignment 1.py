myList = list(map(int, input("Enter the integers (space separated) : ").split()))
myRevList = []

for i in range(len(myList)-1, -1, -1):
    myRevList.append(myList[i])

sumList = []
for i in range(len(myList)):
    sumList.append(myList[i] + myRevList[i])

print(sumList)
