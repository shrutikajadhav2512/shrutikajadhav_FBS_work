# WAP to print Fibonacci series using recursion.
def fibo(n,a=-1,b=1):
        if(n>0):
            c=a+b
            print(c,end=' ')
            return fibo(n-1,b,c)
n=int(input('Enter number:'))
fibo(n)
