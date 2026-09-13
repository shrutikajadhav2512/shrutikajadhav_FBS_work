import demo1
def usit():
    print("I am in usit")
    print(__name__)
    demo1.add()
if(__name__=="__main__"):
    usit()