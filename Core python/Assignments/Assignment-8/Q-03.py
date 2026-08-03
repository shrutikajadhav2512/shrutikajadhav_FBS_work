# WAP to find sum of following series using function
# a.1+2+3+4+.....+n
# b.1!+2!+3!+.....+n!
# c.1^1+2^2+3^3+.....+n^n

# a.1+2+3+4+.....+n
def series(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
n=int(input('1+2+3+4+....+n.enter last number(n):'))
result=series(n)
print(f'sum of 1 to {n} = {result}')
print()

#  b.1!+2!+3!+.....+n!
def factorial(a):
    sum=0
    fact=1
    for i in range(1,a+1):
        fact=fact*i
        sum=sum+fact
    return sum
a=int(input('1 to n factorial,enter end value(n):'))
res=factorial(a)
print(f'sum of 1 to {a} factorial is {res}')
print()

# c.1^1+2^2+3^3+.....+n^n
def power(x):
    sum=0
    for i in range(1,x+1):
        sum=sum+i**i
    return sum
x=int(input('1^1+2^2+3^3+....+n^n.Enter last number(n):'))
display=power(x)
print(f'sum of 1^1 to {x}^{x} = {display}')

