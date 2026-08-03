# sum of all numbers between 1 to n.
def odd(n):
    sum=0
    for i in range(1,n+1):
        if(i%2!=0):
            print(i)
            sum=sum+i
    return sum

n=int(input('1+3+5.....+n.enter last value(n):'))
result=odd(n)
print(f'sum of odd number 1 to {n} = {result}')