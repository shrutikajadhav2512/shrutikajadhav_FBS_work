def greet():
    no=int(input('enter a number:'))
    temp=no
    rev=0
    while(temp>0):
        d=temp%10
        temp=temp//10
        rev=rev*10+d
    if(no==rev):
        print(f'{no} is a palindrome')
    else:
        print(f'{no} is not palindrome')
greet()