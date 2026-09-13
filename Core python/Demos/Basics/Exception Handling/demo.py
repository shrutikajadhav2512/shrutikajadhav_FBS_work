#Write a program to take two no and input from user and print division
try:
    num1=int(input("Enter number 1:"))
    num2=int(input("Enter number 2:"))
    print("division=",num1//num2)
    
except ZeroDivisionError as z:
    print(z)
except ValueError as v:
    print("Enter Proper Intiger Value.")
except Exception as e:
    print("Can not divide by zero.")
else:
    print("Not exception in your code..")
