# WAP to find sum of n number using recursion
def add(n):
    if(n==0):
        return 0
    else:
        return n+add(n-1)
n=int(input('Enter a number:'))
res=add(n)
print(f'sum of 1 to {n}={res}')