# WAP to find print the following fibonacci series using function
# 1 1 2 3 5 8 
def fibonacci(n):
    a=-1
    b=1
    for i in range(1,n+1):
        c=a+b
        print(c)
        a=b
        b=c
print('Fibonacci series.')
n=int(input('Enter number:'))
fibonacci(n)
