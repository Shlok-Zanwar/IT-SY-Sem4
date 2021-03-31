class Student:
    def __init__(self, id, name, maths, science, english):
        self.id = id
        self.name = name
        self.maths = maths
        self.science = science
        self.english = english

    def doCalculations(self):
        if self.maths >= 50 and self.science >= 50 and self.english >= 50:
            percent = (self.maths + self.science + self.english)/3
            if percent >= 75:
                return "A"
            elif percent >= 60:
                return "B"
            else:
                return "C"

        else:
            return "Fail"


students = []

students.append(Student(1, "John Cena", 85, 74, 90))
students.append(Student(2, "Brock Lesnar", 45, 30, 55))
students.append(Student(3, "Randy Orton", 67, 74, 60))
students.append(Student(4, "Rey Mysterio", 55, 52, 58))
students.append(Student(5, "The Rock", 85, 92, 90))
students.append(Student(6, "Sin Cara", 36, 33, 60))


for student in students:
    print("Id      : ", student.id)
    print("Name    : ",  student.name)
    print("Maths   : ",  student.maths)
    print("Science : ", student.science)
    print("English : ", student.english)
    print("\nGrade   : ", student.doCalculations())

    print("\n----------------------------------------------------\n")
