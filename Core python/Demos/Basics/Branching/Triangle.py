# input angles of triangles and check it is valid or not
# take input 3 angles for triangels
a=float(input('Enter angle1:'))
b=float(input('Enter angle2:'))
c=float(input('Enter angle3:'))

if(a+b+c==180):
    print('It is valid triangle')
else:
    print('It is not valid triangle')
