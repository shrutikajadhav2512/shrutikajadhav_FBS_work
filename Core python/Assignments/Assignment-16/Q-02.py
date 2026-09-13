# Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowProduct
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:
    discount = 10
    # Constructor
    def __init__(self,pid=1,pname="Laptop",price=50000,quantity=1):
        self.PId=pid
        self.PName=pname
        self.Price=price
        self.Quantity=quantity
    # Getter and Setter
    def getId(self):
        return self.PId
    def setId(self,newPId):
        self.PId=newPId
    def getPName(self):
        return self.PName
    def setPName(self,newPname):
        self.PName=newPname
    def getPrice(self):
        return self.Price
    def setPrice(self,newPrice):
        self.Price=newPrice
    def getQuantity(self):
        return self.Quantity
    def setQuantity(self,newQuantity):
        self.Quantity=newQuantity

    def applyDiscount(self):
        self.Price = self.Price - (self.Price * Product.discount / 100)
    # Destructor
    def __del__(self):
        print(f"Product Object Destroyed.")
    # Display showBook
    def showProduct(self):
        return f"Product Id={self.PId}      Product Name={self.PName},     Product Price={self.Price},     Product Quantity={self.Quantity}"
b1=Product(2,"Mobile",20000,2)
b2=Product(3,"Headphones",10000,4)
print("before discount.")
print(b2.showProduct())
b2.applyDiscount()
print("after discount.")
print(b2.showProduct())

# print(b2.applyDiscount())
b3=Product()
print(b3.showProduct())
print(f"Discount Product={Product.discount}%")


