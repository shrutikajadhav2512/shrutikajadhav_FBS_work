# Write a program to find factorial of given number using recursion
def factorial(num):
    if(num>1):
        return num*factorial(num-1)
    else:
        return 1
num=int(input("Enter the number:"))
res=factorial(num)
print(f"Factorial is={res}")