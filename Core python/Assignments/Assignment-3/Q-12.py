# WAP to check if given 3digit 
# number is a palindrome or not.

# take input enter 3 digit number
num=int(input('Enter 3 digit number:'))

if(100<=num<=999):
    firstdigit=num//100
    lastdigit=num%10
    if(firstdigit==lastdigit):
        print(f'{num} this is palindrome number')
    else:
        print(f'{num} this is not palindrome number')

else:
    print('Enter 3 digit number')
