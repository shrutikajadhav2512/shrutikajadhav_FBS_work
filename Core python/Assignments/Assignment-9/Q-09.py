# WAP to calculate the m to the power n using recursion
def power(m,n):
    if(n==0):
        return 1
    return m*power(m,n-1)
m=int(input('enter the value of m:'))
n=int(input('enter the value of n:'))
result=power(m,n)
print(f'{m}**{n}={result}')