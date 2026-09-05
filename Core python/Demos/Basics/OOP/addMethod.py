# a=10
# b=20
# print(a+b)
# a="abc"
# b="xyz"
# print(a+b)
# li1=[1,2,3,4]
# li2=[5,7,6,8]
# print(li1+li2)
class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
    def getHr(self):
        return self.hr
    def setHr(self,newMin):
        self.hr=newMin
    def getMin(self):
        return self.min
    def setMin(self,newMin):
        self.min=newMin
    def getSec(self):
        return self.sec
    def setSec(self,newSec):
        self.sec=newSec
    def __add__(self, other):
        totalsec=self.sec+other.sec
        remmin=totalsec//60
        totalsec=totalsec%60
        totalmin=self.min+other.min+remmin
        remHr=totalmin//60
        totalmin=totalmin%60
        totalhr=self.hr+other.hr+remHr
        return Time(totalhr,totalmin,totalsec)
    def __str__(self):
        return f"hr={self.hr},Min={self.min},Sec={self.sec}"
    
t1=Time(2,45,50)
t2=Time(3,20,30)
print(t1+t2)
