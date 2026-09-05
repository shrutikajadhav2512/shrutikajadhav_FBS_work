class Product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price
    def getId(self):
        return self.id
    def setId(self,newId):
        self.id=newId
    def getName(self):
            return self.name
    def setName(self,newName):
            self.name=newName
    def getPrice(self):
            return self.price
    def setPrice(self,newPrice):
            self.price=newPrice
    def display(self):
        print(f"id={self.id},name={self.name},price={self.price}")
p1=Product(1,"TV",65000)
p2=Product(2,"Watch",10000)
p1.setPrice(50000)
print(p1.getPrice())