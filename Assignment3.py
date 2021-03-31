print("Assignment for read, write and append operations")

print("\nCreating a new file (details.txt) and adding 5 entries using 'w+'.")

details = []
for i in range(5):
    name = input("\nEnter name : ")
    age = input("Enter age  : ")
    details.append(name)
    details.append(age)

fWrite = open("details.txt", "w+")
for line in details:
    fWrite.write(line + "\n")
fWrite.close()

print("\nAppending next 5 entries to (details.txt) using 'a+'")

fAppend = open("details.txt", "a+")
for i in range(5):
    name = input("\nEnter name : ")
    age = input("Enter age  : ")
    fAppend.write(name + "\n")
    fAppend.write(age + "\n")
fAppend.close()

print("\nReading all data from (details.txt) using 'r' \n")
fRead = open("details.txt", "r")
lines = fRead.readlines()

for i in range(0, len(lines), 2):
    print("Detail {}\t:\t {}\t{} " .format(int(i/2) + 1, (lines[i]).strip(), (lines[i+1]).strip()) )



