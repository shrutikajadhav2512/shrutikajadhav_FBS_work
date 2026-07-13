# largest of three number
# take three no a,b,c
print('Enter three no.then find large number.')
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
c=int(input('Enter 3rd number:'))
# calculations
if(a>b and a>c):
    print(f'{a} is large')
elif(b>a and b>c):
    print(f'{b} is large')
else:
    print(f'{c} is large')
