# Create a class College which has collection of students. Add the
# following methods :
# a. Parameteried constructor for number of students.
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override __str__ Method
class College:
    def __init__(self, number_of_students):
        self.details = {}
        self.number_of_students = number_of_students
    def getNoOfStudent(self):
        return self.number_of_students
    def setNoOfStudent(self,newNoOfStudent):
        self.number_of_students=newNoOfStudent
    
    def AddStudent(self):
        rollno = input("Enter Roll No: ")
        name = input("Enter Name: ")
        self.details[rollno] = name
    
    def GetStudent(self):
        rollno = input("Enter Roll No: ")

        if rollno in self.details:
            return self.details[rollno]
        else:
            return "Student not found"
    
    def RemoveStudent(self):
        rollno = input("Enter Roll No: ")

        if rollno in self.details:
            del self.details[rollno]
            return "Student removed successfully"
        else:
            return "Roll No is not present"
    def __str__(self):
        return str(self.details)

c = College(3)
c.AddStudent()
c.AddStudent()
print(c.GetStudent())
print(c.RemoveStudent())
print(c)
