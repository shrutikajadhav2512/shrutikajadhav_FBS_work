# WAP to prompt user to enter userid and password
# after verifying userid and password display a 4 digit
# random number and ask user to enter the same.if user enters 
# the same number then show him success mesage otherwise failed
# (something like captcha)
import random
# take input userid and password
userId=input('Enter userId:')
password=input('Enter password:')

if(userId=='Admin' and password=='1234'):  
    captch=random.randint(1000,9999)
    print(f'This is your captcha:{captch}')
    captcha=int(input('Please enter captcha:'))
    if(captch==captcha):
        print('Login success')
    else:
        print('Login failed')
else:
    print('invalid userId and password')
