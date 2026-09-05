# Hirarachical inheritance
class Emp:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.salary=sal
    def getId(self):
        return self.id
    def setId(self,newId):
        self.id=newId
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName
    def getSal(self):
        return self.salary
    def setSal(self,newSal):
        self.salary=newSal
    def calculateSalary(self):
        return self.salary
    def __str__(self):
        return f"ID={self.id}, Name={self.name}, sal={self.salary}"
# Emp class is over.....
class Hr(Emp):
    def __init__(self, id, name, sal,commission):
        super().__init__(id, name, sal)
        self.Commission=commission
    def getCommission(self):
        return self.Commission
    def setCommission(self,newCommission):
        self.Commission=newCommission
    def calculateSalary(self):
        return self.salary+self.Commission
    def __str__(self):
        return super().__str__()+f" Commision={self.Commission}"
# Hr class is over.....
class JuniorHr(Hr):
    def __init__(self, id, name, sal, commission):
        super().__init__(id, name, sal, commission)
        print("I am junior Hr..")
# JuniorHr class is over.....
class SeniorHr(Hr):
    def __init__(self, id, name, sal, commission):
        super().__init__(id, name, sal, commission)
        print("I am senior Hr..")
# SeniorHr class is over.....
class Dev(Emp):
    def __init__(self, id, name, sal,bonus):
        super().__init__(id, name, sal)
        self.bonus=bonus
    def getBonus(self):
        return self.bonus
    def setBonus(self,newBonus):
        self.bonus=newBonus
    def calculateSalary(self):
        return self.salary+self.bonus
    def __str__(self):
        return super().__str__()+f" Bonus={self.bonus}"
# Dev class is over.....
class JuniorDev(Dev):
    def __init__(self, id, name, sal, bonus):
        super().__init__(id, name, sal, bonus)
        print("I am Junior Developer..")
# JuniorDev class is over.....  
class SeniorDev(Dev):
    def __init__(self, id, name, sal, bonus):
        super().__init__(id, name, sal, bonus)
        print("I am Senior Developer..")
# SenoirDev class is over.....
e1=Emp(1,"Raj",356788)
h1=Hr(2,"Ram",23456,3456)
d1=Dev(3,"Radha",1554656,7846)
j1=JuniorDev(4,"Anjali",3567,56789)
s1=SeniorDev(5,"Rohit",34568,3546)
sh1=SeniorHr(6,"Virat",35678,6245)
jh1=JuniorHr(7,"Dipali",7563529,758694)
print(e1)
print(h1)
print(d1)
print(j1)
print(s1)
print(sh1)
print(jh1)
print(d1.calculateSalary())
print(jh1.calculateSalary())

