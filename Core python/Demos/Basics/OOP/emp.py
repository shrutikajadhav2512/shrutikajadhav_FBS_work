from abc import ABC,abstractmethod
class Emp(ABC):
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
    @abstractmethod
    def calculateSalary(self):
        pass
    def __str__(self):
        return f"ID={self.id}, Name={self.name}, sal={self.salary}"
    # def display(self):
    #     print(f"id={self.id},Name={self.name},Salary={self.salary}")
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
# e1=Emp(1,"abc",356788)
h1=Hr(2,"xyz",23456,3456)
d1=Dev(3,"pqr",1554656,7846)
print(h1.calculateSalary())
print(d1.calculateSalary())
# print(e1.calculateSalary())
# print(d1.getName())
# print(h1.getCommission())
# print(e1)
print(h1)
print(d1)

