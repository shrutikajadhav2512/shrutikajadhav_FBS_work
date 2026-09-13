def add():
    print("I am in addition")
    print(__name__)
def sub():
    print("I am in substraction")
if(__name__=="__main__"):
    add()
    sub()
    print(__name__)