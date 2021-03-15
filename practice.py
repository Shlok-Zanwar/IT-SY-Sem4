# noOfRows = int(input("Enter number of rows : "))
# matrix = []
# for i in range(noOfRows):
#     # row = list(map(int, input().split()))
#     row = input().split()
#     for j in range(len(row)):
#         row[j] = int(row[j])
#     matrix.append(row)
#
# print(matrix)
#
# def checkSymm(matrix, noOfRows):
#     for i in range(noOfRows):
#         for j in range(noOfRows):
#             if matrix[i][j] != matrix[j][i]:
#                 return False
#
#     return True
#
#
# print(checkSymm(matrix, noOfRows))


# noOfCases = int(input())

# myList = []

# for i in range(noOfCases):
#     arr = input().split()
#     arr[1] = int(arr[1])

#     notFound = True
#     for j in range(len(myList)):
#         if myList[j][0] == arr[0]:
#             myList[j][1] += arr[1]
#             myList[j][2] = i
#             notFound = False
#             break

#     if notFound:
#         arr.append(i)
#         myList.append(arr)

# myList.sort(key=lambda x: x[1], reverse=True)

# myMax = myList[0][1]
# myName = myList[0][0]
# myIndex = myList[0][2]

# for i in range(1, len(myList)):
#     if myList[i][1] != myMax:
#         break

#     if myList[i][2] < myIndex:
#         myName = myList[i][0]
#         myIndex = myList[i][2]

# print(myName)
# print(myList)

# string = input("String : ")
# toSearch = input("To Search : ");

# index = 0

# for i in range (0, len(string)):
#     if string[i] == toSearch[index]:
#         index += 1 
#         if index == len(toSearch):
#             print("Found")
#             break
#     else:
#         index = 0

# if i == len(string) - 1:
#     print("Not Found")

# import datetime
# import calendar

# current_time = "2021-02-15T11:58:23.588826+05:30"
# # a = datetime.

# year = current_time[0:4]
# month = current_time[5:7]
# day = current_time[8:10]

# # myDate = datetime.date(int(year), int(month), int(day)).strftime("%b");

# print(calendar.month_name[int(month)]);


# import win32com.clie
