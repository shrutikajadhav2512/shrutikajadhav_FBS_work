# WAP to check if given number is armstrong number or not
no=int(input('Enter the number:'))
count=len(str(no))
temp=no
total=0
while(no>0):
    d=no%10
    total=total+(d**count)
    no=no//10
print(total)
if(total==temp):
    print('the number is armstrong')
else:
    print('the number is not armstrong')