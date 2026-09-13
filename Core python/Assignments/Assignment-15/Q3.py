# Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowShirt
class Shirt:
    # Constructor
    def __init__(self, sid=1, sname="Peter England", type="Formal", price=1500, size="Large"):
        self.SId = sid
        self.SName = sname
        self.Type = type
        self.Price = price
        self.Size = size

    # Getter and Setter
    def getId(self):
        return self.SId

    def setId(self, newSId):
        self.SId = newSId

    def getSName(self):
        return self.SName

    def setSName(self, newSName):
        self.SName = newSName

    def getType(self):
        return self.Type

    def setType(self, newType):
        self.Type = newType

    def getPrice(self):
        return self.Price

    def setPrice(self, newPrice):
        self.Price = newPrice

    def getSize(self):
        return self.Size

    def setSize(self, newSize):
        self.Size = newSize

    # Destructor
    def __del__(self):
        print("Shirt Object Destroyed.")

    # Display Shirt
    def showShirt(self):
        return f"Shirt Id={self.SId}      Shirt Name={self.SName},      Shirt Type={self.Type},      Shirt Price={self.Price},      Shirt Size={self.Size}"


# Parameterized constructor
s1 = Shirt(2, "Raymond", "Formal", 2000, "Large")
print(s1.showShirt())

s2 = Shirt(3, "Levis", "Casual", 1800, "Medium")
print(s2.showShirt())

# Parameterless constructor
s3 = Shirt()
print(s3.showShirt())
