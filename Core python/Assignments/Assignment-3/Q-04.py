# WAP to input all sides of a triangle and check whether triangle is valid or not
# take input from user 
a=int(input('Enter side1:'))
b=int(input('Enter side2:'))
c=int(input('Enter side3:'))

if(a+b>c and b+c>a and c+a>b):
    print('Valid triangle')
else:
    print('Invalid triangle')