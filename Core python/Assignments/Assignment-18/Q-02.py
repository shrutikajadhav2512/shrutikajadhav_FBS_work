# Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator
class Distance:
    def __init__(self,km,m,cm):
        self.km=km
        self.m=m
        self.cm=cm
    def getkm(self):
        return self.km
    def setkm(self,newkm):
        self.km=newkm
    def getm(self):
        return self.m
    def setm(self,newm):
        self.m=newm
    def getcm(self):
        return self.cm
    def setcm(self,newcm):
        self.cm=newcm
    def __del__(self):
        print("I am Destructor")
    def __add__(self, other):
        km=self.km+other.km
        m=self.m+other.m
        cm=self.cm+other.cm
        if cm >= 100:
            m = m + cm // 100
            cm = cm % 100
        if m >= 1000:
            km = km + m // 1000
            m = m % 1000
        return Distance(km,m,cm)
    def __sub__(self, other):
        km=self.km-other.km
        m=self.m-other.m
        cm=self.cm-other.cm
        if cm < 0:
            m = m - 1
            cm = cm + 100
        if m < 0:
            km = km - 1
            m = m + 1000
        return Distance(km,m,cm)
    def __str__(self):
        return f"km={self.km},m={self.m},cm={self.cm}"
d1=Distance(100,120,200)
d2=Distance(50,20,7)
d3=d1+d2
d4=d1-d2
print(d3)
print(d4)
