# multiple inheritance
class Mechanical:
    def __init__(self):
        print("I am from Mechanical..")
    def __str__(self):
        return "Mechanical object.."
    def getBranch(self):
        print("Mechanical Branch..")
# Mechanical class is over
class Electric:
    def __init__(self):
        print("I am from Electric..")
    def __str__(self):
        return "Object of Electic.."
    def getBranch(self):
        print("Electical Branch..")
class Mecatronix(Mechanical,Electric):
    def __init__(self):
        super().__init__()
        print("cont of mecatronix get called")
    def __str__(self):
        return super().__str__()+"\nObject of Mecatronix"
    def getBranch(self):
        print("Mecatronix Branch..")
m=Mecatronix()
print(m)
print(m.getBranch())