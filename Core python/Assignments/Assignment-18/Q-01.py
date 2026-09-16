#  Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator
class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def getReal(self):
        return self.real
    def setReal(self,newReal):
        self.real=newReal
    def getImag(self):
        return self.imag
    def setImag(self,newImag):
        self.imag=newImag
    def __del__(self):
        print("This is oparator overloading")
    def __add__(self, other):
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return Complex(new_real, new_imag)
    def __sub__(self, other):
        newreal=self.real-other.real
        newimag=self.imag-other.imag
        return Complex(newreal,newimag)
    def __str__(self):
        return f"real={self.real},imag={self.imag}"
c1=Complex(3,2)
c2=Complex(7,4)
c3=c1+c2
print(c3)
c4=c1-c2
print(c4)