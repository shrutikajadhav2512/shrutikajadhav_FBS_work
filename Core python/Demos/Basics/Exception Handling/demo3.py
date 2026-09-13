try:
    no1=int(input("Enter the number 1:"))
    no2=int(input("Enter the number 2:"))
    if(no2<=0):
        raise Exception("wrong input")
    else:
        print(no1//no2)
except Exception as e:
    print(e)