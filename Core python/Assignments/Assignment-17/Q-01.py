# Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method
class Student:
    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage
    def getStudentId(self):
        return self.StudentId
    def setStudentId(self,newid):
        self.StudentId=newid
    def getName(self):
        return self.Name
    def setName(self,newName):
        self.Name=newName
    def getPercentage(self):
        return self.Percentage
    def setPercentage(self,newpercentage):
        self.Percentage=newpercentage
    def getAge(self):
        return self.Age
    def setAge(self,newAge):
        self.Age=newAge  

    def Display(self):
        print("Student ID:", self.StudentId)
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Percentage:", self.Percentage)
        print("Rank:", self.CalculateRank())

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
        elif self.Percentage >= 40:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return (f"Student ID: {self.StudentId}, "
                f"Name: {self.Name}, "
                f"Age: {self.Age}, "
                f"Percentage: {self.Percentage}")
s = Student(101, "Rahul", 20, 82.5)
print(s.Accept())
print(s.Display())
print("\nUsing __str__ method:")
print(s)
