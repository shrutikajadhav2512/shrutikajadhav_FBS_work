# WAP to check whether the triangle is 
# equilateral,isosceles or scalene triangle
# take input sides from user
a=int(input('Enter side1:'))
b=int(input('Enter side2:'))
c=int(input('Enter side3:'))
if(a==b==c):
    print('This is equilateral triangle') 
elif(a == b or b == c or a == c):
    print('This is isosceles triangle')
else:
    print('This is scalene triangle') #  (a != b and b != c and a != c)