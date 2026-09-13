# Create a derived class from Student as EnggStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method

class Student:
    def __init__(self, rollno, name, marks):
        self.RollNo = rollno
        self.Name = name
        self.Marks = marks
    def getRollNo(self):
        return self.RollNo
    def setRollNo(self,newRollNo):
        self.RollNo=newRollNo
    def getName(self):
        return self.Name
    def setName(self,newName):
        self.Name=newName
    def getMarks(self):
        return self.Marks
    def setMarks(self,newMarks):
        self.Marks=newMarks

    def CalculateRank(self):
        if self.Marks >= 75:
            return "Distinction"
        elif self.Marks >= 60:
            return "First Class"
        elif self.Marks >= 50:
            return "Second Class"
        elif self.Marks >= 35:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"Roll No={self.RollNo}, Name={self.Name}, Marks={self.Marks}"

class EnggStudent(Student):

    # Parameterized Constructor
    def __init__(self, rollno, name, marks, branch, internalMarks):
        super().__init__(rollno, name, marks)
        self.Branch = branch
        self.InternalMarks = internalMarks
    def getBranch(self):
        return self.Branch
    def setBranch(self,newBranch):
        self.Branch=newBranch
    def getInternalMarks(self):
        return self.InternalMarks
    def setInternalMarks(self,newInternalMarks):
        self.InternalMarks=newInternalMarks
    # Accept
    def Accept(self):
        self.RollNo = int(input("Enter Roll No: "))
        self.Name = input("Enter Name: ")
        self.Marks = float(input("Enter External Marks: "))
        self.Branch = input("Enter Branch: ")
        self.InternalMarks = float(input("Enter Internal Marks: "))

    # Display
    def Display(self):
        return f"Roll No = {self.RollNo} Name = {self.Name} Marks = {self.Marks} Branch = {self.Branch} Internal Marks = {self.InternalMarks} Rank = {self.CalculateRank()}"

    # Override CalculateRank
    def CalculateRank(self):
        totalMarks = self.Marks + self.InternalMarks

        if totalMarks >= 75:
            return "Distinction"
        elif totalMarks >= 60:
            return "First Class"
        elif totalMarks >= 50:
            return "Second Class"
        elif totalMarks >= 35:
            return "Pass"
        else:
            return "Fail"

    # Override __str__
    def __str__(self):
        return f"Roll No={self.RollNo}, Name={self.Name}, Marks={self.Marks}, Branch={self.Branch}, Internal Marks={self.InternalMarks}"


# Create object using parameterized constructor
e1 = EnggStudent(1, "Rahul", 65, "Computer", 15)
print(e1.Display())
print(e1.Accept())
print(e1)
