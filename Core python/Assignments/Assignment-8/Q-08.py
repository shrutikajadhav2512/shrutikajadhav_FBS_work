# WAP find reverse of a number
def reverse(n):
    rev=0
    while(n>0):
        d=n%10
        n=n//10
        rev=rev*10+d
    print(f'The reverse number is {rev}')
n=int(input('Enter a number:'))
reverse(n)