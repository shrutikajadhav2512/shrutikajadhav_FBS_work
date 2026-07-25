# WAP to prompt user to enter userid and password.
# if id and password is incorrect give him chance
#  to re-enter the credentials.let him try 3 times.
#  after the progeam to terminate.

Userid='abc123'
Pasword=9876

for i in range(1,4):
    userid=(input('enter userid:'))
    pasword=int(input('enter password:'))
    if(Userid==userid and Pasword==pasword):
        print("login successful.")
        break
    