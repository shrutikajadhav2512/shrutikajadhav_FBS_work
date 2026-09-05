# multilevel inheritance
class Person:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    def getId(self):
        return self.id
    def setId(self,newId):
        self.id=newId
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName
    def getAge(self):
        return self.age
    def setAge(self,newAge):
        self.age=newAge
    def __str__(self):
        return f"ID={self.id},      Name={self.name},       Age={self.age}"
# Person class is over
class Student(Person):
    def __init__(self, id, name, age,clas):
        super().__init__(id, name, age)
        self.Class=clas
    def getClass(self):
        return self.clas
    def setClass(self,newClas):
        self.Class=newClas
    def __str__(self):
        return super().__str__()+f"      class={self.Class}"
# Student class is over
class Teacher(Student):
    def __init__(self, id, name, age,clas,subName):
        super().__init__(id, name, age,clas)
        self.Subname=subName
    def getSubName(self):
        return self.Subname
    def setSubName(self,newSubName):
        self.Subname=newSubName
    def __str__(self):
        return super().__str__()+f"     Subname={self.Subname}"
# Teacher class is over
p1=Person(3,"abc",30)
s1=Student(2,"anjali",12,"5th")
t1=Teacher(1,"raj",55,"10th","English")
print(t1)
print(s1)
print(p1)
    