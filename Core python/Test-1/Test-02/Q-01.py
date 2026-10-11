year=int(input("Enter year for check leap year or not:"))
if(year%4!=0):
    print(year,"is not a leap year.")
else:
    if(year%100!=0):
        print(year,"is a leap year.")
    else:
        if(year%4!=0):
            print(year,"is not a leap year.")
        else:
            print(year,"is a leap year.")