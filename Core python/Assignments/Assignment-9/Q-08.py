# Write a program to check whether a number is 
# prime or not using recursion.
def prime(n,i=2):
    if(n<=1):
        return False
    if(i==n):
        return True
    if(n%i==0):
        return False
    return prime(n,i+1)
n=int(input('Enter a number to check prime or not:'))
res=prime(n)
if(res==True):
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')