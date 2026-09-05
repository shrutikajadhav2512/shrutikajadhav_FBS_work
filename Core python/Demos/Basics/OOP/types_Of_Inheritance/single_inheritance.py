class Person:
    def __init__(self,id,name):
        self.Name=name
        self.Id=id
    def getName(self):
        return self.Name
    def setName(self,newName):
        self.Name=newName
    def getId(self):
        return self.Id
    def setName(self,newId):
        self.Id=newId
    def __str__(self):
        return f"Name={self.Name},      Id={self.Id},"
# Person class is over
class Student(Person):
    def __init__(self, id, name,rollNo):
        super().__init__(id, name)
        self.RollNo=rollNo
    def getRollNo(self):
        return self.RollNo
    def setRollNo(self,newRollNo):
        self.RollNo=newRollNo
    def __str__(self):
        return super().__str__()+f"     RollNo={self.RollNo}."
s1=Student(1,"shrutika",35)
print(s1)
