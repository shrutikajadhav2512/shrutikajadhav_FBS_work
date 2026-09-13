# Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBookd. 
# d. Add static variable count and also maintain count of objects created.
class Book:
    count=0
    # Constructor
    def __init__(self,bid=1,bname="Shyamchi Aai",price=100,author="Sane Guruji"):
        self.BId=bid
        self.BName=bname
        self.Price=price
        self.Author=author
        Book.count+=1
    # Getter and Setter
    def getId(self):
        return self.BId
    def setId(self,newBId):
        self.BId=newBId
    def getBName(self):
        return self.BName
    def setBName(self,newBname):
        self.BName=newBname
    def getPrice(self):
        return self.Price
    def setPrice(self,newBPrice):
        self.Price=newBPrice
    def getAuthor(self):
        return self.Author
    def setAuthor(self,newAuthor):
        self.Author=newAuthor
    # Destructor
    def __del__(self):
        print("A good book is a good friend.")
    # Display showBook
    def showBook(self):
        return f"Book Id={self.BId}      Book Name={self.BName},     Book Price={self.Price},     Book Author={self.Author}"
b1=Book(1,"Think And Grow Rich",200,"Nepolian Hill")
b2=Book(2,"Mrutyunjay",500,"Shivaji Sawant")
print(b2.showBook())
b3=Book()
print(b3.showBook())
print(f"total books={Book.count}")

