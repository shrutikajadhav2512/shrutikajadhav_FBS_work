class Person:
    def __init__(self,id,name,age,address):
        self.id=id
        self.name=name
        self.age=age
        self.address=address
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
    def getIAddress(self):
        return self.address
    def setAddress(self,newAddress):
        self.address=newAddress
    def display(self):
        print(f"Id={self.id},Name={self.name},Age={self.age},Address={self.address}")
p1=Person(1,"abc",25,"Pune")
p2=Person(2,"xyz",22,"Kolhapur")
p1.setAge(26)
print(p1.getAge())
