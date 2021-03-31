rows1 = int(input("Enter number of rows in matrix 1: "))
columns1 = int(input("Enter number of coulmns in matrix 1: "))
rows2 = int(input("Enter number of rows in matrix 2: "))
columns2 = int(input("Enter number of coulmns in matrix 2: "))
enteredmatrix1 = []
enteredmatrix2 = []
transposedmatrix1 = []
transposedmatrix2 = []
resmatrix = []


def acceptmatr(enteredmatrix, rows, columns):
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(int(input("Enter a{}{}: ".format(i, j))))
        enteredmatrix.append(temp)


def showmat(matr, rows, columns):
    for i in range(rows):
        for j in range(columns):
            print(matr[i][j], end="  ")
        print()


def transposematr(enteredmatrix, transposedmatrix, rows, columns):
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(enteredmatrix[j][i])
        transposedmatrix.append(temp)


def checksymmetry(enteredmatrix, transposedmatrix, rows, columns):
    if(rows != columns):
        return False
    else:
        for i in range(rows):
            for j in range(columns):
                if(enteredmatrix[i][j] != transposedmatrix[i][j]):
                    return False
        return True


def addmat(enteredmatrix1, enteredmatrix2, rows, columns):
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(enteredmatrix1[i][j]+enteredmatrix2[i][j])
        resmatrix.append(temp)
    showmat(resmatrix, rows, columns)


def submat(enteredmatrix1, enteredmatrix2, rows, columns):
    resmatrix = []
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(enteredmatrix1[i][j]-enteredmatrix2[i][j])
        resmatrix.append(temp)
    showmat(resmatrix, rows, columns)


def mulmat(enteredmatrix1, enteredmatrix2):
    resmatrix = []
    for i in range(columns1):
        temp = []
        for j in range(rows2):
            tempadd = 0
            for k in range(columns2):
                tempadd = tempadd+(enteredmatrix1[i][k]*enteredmatrix2[k][j])
            temp.append(tempadd)
        resmatrix.append(temp)
    showmat(resmatrix, rows1, columns2)


# Accept matrices
print("\nFor Matrix 1 :-")
acceptmatr(enteredmatrix1, rows1, columns1)
print("\nFor Matrix 2 :-")
acceptmatr(enteredmatrix2, rows2, columns2)

# Display entered matrices
print("\nEntered matrix 1 is:-")
showmat(enteredmatrix1, rows1, columns1)
print("Entered matrix 2 is:-")
showmat(enteredmatrix2, rows2, columns2)

# Calculate and display Transpose of the matrices
print("\nTranspose of matrix 1 is:-")
transposematr(enteredmatrix1, transposedmatrix1, rows1, columns1)
showmat(transposedmatrix1, rows1, columns1)
print("Transpose of matrix 2 is:-")
transposematr(enteredmatrix2, transposedmatrix2, rows2, columns2)
showmat(transposedmatrix2, rows2, columns2)

# Check symmetry of the matrices
print()
if(checksymmetry(enteredmatrix1, transposedmatrix1, rows1, columns1)):
    print("Matrix 1 is symmetric.")
else:
    print("Matrix 1 is not symmetric.")
if(checksymmetry(enteredmatrix1, transposedmatrix1, rows2, columns2)):
    print("Matrix 2 is symmetric.")
else:
    print("Matrix 2 is not symmetric.")

#Addition and Subtraction
if(rows1 == rows2 and columns1 == columns2):
    print("\nAddition:-")
    addmat(enteredmatrix1, enteredmatrix2, rows1, columns1)
    print("\nSubtraction:-")
    submat(enteredmatrix1, enteredmatrix2, rows1, columns1)
else:
    print("Addition and subtraction not possible.")

# Multiplication
if(columns1 == rows2):
    print("\nMultiplication:-")
    mulmat(enteredmatrix1, enteredmatrix2)
else:
    print("\nCannot multiply the given matrices")