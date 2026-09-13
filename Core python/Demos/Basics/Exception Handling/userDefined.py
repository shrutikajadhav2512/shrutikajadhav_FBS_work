from myException import MyException
try:
    no1=int(input("Enter the number 1:"))
    no2=int(input("Enter the number 2:"))
    if(no2<=0):
        raise MyException()
    else:
        print(no1//no2)
except MyException as m:
    print("My Exception")
except Exception as e:
    print(e)