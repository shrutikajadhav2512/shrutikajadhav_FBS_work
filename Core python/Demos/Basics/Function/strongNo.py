# check strong number or not
def strongNo():
    no=int(input('Enter a number:'))
    temp=no
    sum=0
    while(temp>0):
        d=temp%10
        temp=temp//10
        fact=1
        for i in range(1,d+1):
            fact=fact*i
        sum=sum+fact
    if(no==sum):
        print(f'{no} is strong number')
    else:
        print(f'{no} is not a strong number')
strongNo()