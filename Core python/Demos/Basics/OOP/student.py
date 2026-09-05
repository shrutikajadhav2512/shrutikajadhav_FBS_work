class FBSStudent:
    stCount=0
    def __init__(self,frn,name,batch):
        self.frn=frn
        self.name=name
        self.batch=batch
        FBSStudent.stCount+=1
    def getId(self):
        return self.frn
    def setId(self,newFrn):
        self.frn=newFrn
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName
    def getBatch(self):
        return self.batch
    def setName(self,newBatch):
        self.batch=newBatch
    def display(self):
        print(f"Id={self.frn},Name={self.name},Batch={self.batch}")
class PlStudent(FBSStudent):
    def __init__(self, frn, name, batch,cName):
        super().__init__(frn, name, batch)
        self.cName=cName
    def getCname(self):
        return self.cName
    def setCname(self,newCname):
        self.cName=newCname
    def display(self):
        super().display()
        print(f"CName={self.cName}")
s1=FBSStudent(1,"abc","June26")
s2=FBSStudent(2,"xyz","June26")
s3=PlStudent(3,"pqr","June25","One8")
print(FBSStudent.stCount)
s3.display()