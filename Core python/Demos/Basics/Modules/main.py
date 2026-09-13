# 1)Direct import
# import cal
# num1=int(input("Enter the num1:"))
# num2=int(input("Enter the num2:"))
# cal.add(num1,num2)
# print(cal.x)

# 2)from module name import member
# from cal import add
# num1=int(input("Enter the num1:"))
# num2=int(input("Enter the num2:"))
# add(num1,num2)
# print()

# 3)from module name import multiple members
# from cal import add,sub,x
# num1=int(input("Enter the num1:"))
# num2=int(input("Enter the num2:"))
# add(num1,num2)
# print(x)
# sub(num1,num2)

# # 4)from module name import all things
# from cal import*
# num1=int(input("Enter the num1:"))
# num2=int(input("Enter the num2:"))
# add(num1,num2)
# print(x)
# sub(num1,num2)


# 5By using alice name
import cal as s
s.add(12,5)
print(s.x)