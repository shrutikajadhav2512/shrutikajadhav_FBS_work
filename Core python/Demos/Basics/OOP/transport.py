class Transport:
    def __init__(self,name,travel):
        self.name=name
        self.travel=travel
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName
    def getTravel(self):
            return self.travel
    def setTravel(self,newTravel):
            self.travel=newTravel
    def dislay(self):
        print(f"name={self.name},travel={self.travel}")
t1=Transport("Car","Road")
t2=Transport("Ship","Water")
t3=Transport("Plane","Air")
t1.setName("bus")
print(t1.getName())
        