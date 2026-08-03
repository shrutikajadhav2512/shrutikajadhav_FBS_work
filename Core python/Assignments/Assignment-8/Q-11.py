# WAP to check if a given number is armstrong number or not.
# for each task create separate function
def checkcount(num):
    count=len(str(num))
    return count
def checkarmstrong(num):
    temp=num
    sum=0
    while(temp>0):
        d=temp%10
        temp=temp//10
        sum=sum+d**checkcount(num)
    return sum

num=int(input('Enter a number to check armstrong or not:'))
res=checkarmstrong(num)
def armstrong(num):
    if(res==num):
        print(f'{num} is armstrong number')
    else:
        print(f'{num} is not armstrong number')
armstrong(num)