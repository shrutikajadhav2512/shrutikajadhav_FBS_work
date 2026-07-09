# WAP to calculate area of triangle and rectangle
# take input for rectangle and triangle
l=int(input('enter length for rectangle:'))
b=int(input('enter breadth for rectangle:'))
base=int(input('enter base for triangle:'))
height=int(input('enter height for triangle:'))
# calculations
rectangle=l*b
triangle=1/2*base*height
print(f'area of rectangle is:{rectangle},area of triangle is:{triangle}')
