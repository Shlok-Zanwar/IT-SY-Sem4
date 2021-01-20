import random

numOfChocolates = 1000
numOfCollections = 50


myList = random.sample(range(1, numOfChocolates), numOfCollections - 1)
myList.sort()
# print(myList)


collections = [myList[0]]
for i in range(1, numOfCollections - 1):
    collections.append(myList[i] - myList[i - 1])
collections.append(numOfChocolates - myList[len(myList) - 1])


print(collections)

for i in range(0, numOfCollections):
    print("collection " + str(i+1) + " : " + str(collections[i]))





