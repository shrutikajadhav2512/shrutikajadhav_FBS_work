# WAP to calculate the area of circle
def Circle(r):
    return 3.14*r**2
radius=int(input('Enter radius for area of circle:'))
area=Circle(radius)
print(f'area of circle is {area} cm')
