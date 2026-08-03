# WAP to calculate area of rectangle
def rectangle(l,b):
    return l*b
length=int(input('Enter length:'))
breadth=int(input('Enter breath:'))
area=rectangle(length,breadth)
print(f'area of rectangle is {area}')