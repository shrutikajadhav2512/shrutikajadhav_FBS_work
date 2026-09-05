class Payment_Mode:
    def __init__(self,id,amount,date):
        self.id=id
        self.amount=amount
        self.date=date
    def getId(self):
        return self.id
    def setId(self,newId):
        self.id=newId
    def getAmount(self):
        return self.amount
    def setAmount(self,newAmount):
        self.amount=newAmount
    def getDate(self):
        return self.date
    def setDate(self,newDate):
        self.date=newDate
    def display(self):
        print(f"Id={self.id},Amount={self.amount},Date={self.date}")
p1=Payment_Mode(1,6000,"24-8-26")
p2=Payment_Mode(2,55000,"23-8-26")
p1.setDate("25-8-26")
print(p1.getDate())