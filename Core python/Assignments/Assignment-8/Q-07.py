# WAP to find sum of digit of a number
def digit(n):
    sum=0
    while(n>0):
        d=n%10
        n=n//10
        sum=sum+d
    print(f'sum of digit is {sum}')
n=int(input('Enter a number:'))
digit(n)


