# Create a class MedicalStudent inherited from Student with following
# :

# i. Data members :Specialization
# ii. MarksOfInternship
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method


class Student:
    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def getStudentId(self):
        return self.StudentId

    def setStudentId(self, newid):
        self.StudentId = newid

    def getName(self):
        return self.Name

    def setName(self, newName):
        self.Name = newName

    def getPercentage(self):
        return self.Percentage

    def setPercentage(self, newpercentage):
        self.Percentage = newpercentage

    def getAge(self):
        return self.Age

    def setAge(self, newAge):
        self.Age = newAge

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def CalculateRank(self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        elif self.Percentage >= 35:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"Student ID={self.StudentId}, Name={self.Name}, Percentage={self.Percentage}"


class MedicalStudent(Student):

    def __init__(self, StudentId, Name, Age, Percentage,
                 Specialization, MarksOfInternship):

        super().__init__(StudentId, Name, Age, Percentage)

        self.Specialization = Specialization
        self.MarksOfInternship = MarksOfInternship

    def getSpecialization(self):
        return self.Specialization

    def setSpecialization(self, newSpecialization):
        self.Specialization = newSpecialization

    def getMarksOfInternship(self):
        return self.MarksOfInternship

    def setMarksOfInternship(self, newMarksOfInternship):
        self.MarksOfInternship = newMarksOfInternship

    def Display(self):
        print("Student ID:", self.StudentId)
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Percentage:", self.Percentage)
        print("Specialization:", self.Specialization)
        print("Marks Of Internship:", self.MarksOfInternship)
        print("Rank:", self.CalculateRank())

    def Accept(self):
        super().Accept()
        self.Specialization = input("Enter Specialization: ")
        self.MarksOfInternship = float(
            input("Enter Marks Of Internship: ")
        )

    def CalculateRank(self):
        total = self.Percentage + self.MarksOfInternship

        if total >= 150:
            return "Distinction"
        elif total >= 120:
            return "First Class"
        elif total >= 100:
            return "Second Class"
        elif total >= 80:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return (f"Student ID={self.StudentId}, "
                f"Name={self.Name}, "
                f"Age={self.Age}, "
                f"Percentage={self.Percentage}, "
                f"Specialization={self.Specialization}, "
                f"Marks Of Internship={self.MarksOfInternship}")


e1 = MedicalStudent(101, "Rahul", 22, 80, "Cardiology", 75)
print(e1.Display())
print(e1.Accept())
print(e1)
