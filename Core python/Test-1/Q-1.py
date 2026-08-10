# WAP to find the area and perimeter to follow(accept the length breadth and radis from user)
def area(w,l,r):
    areaofSquare=l*w
    print(f'areaofSquare={areaofSquare}')
    perimeter=2*(l+w)
    print(f'perimeter={perimeter}')
    area_circle = 3.14*r**2
    print(f'area_circle={area_circle}')

l=int(input('Enter length:'))
w=int(input('Enter breadth:'))
r=int(input('enter radius:'))
res=area(l,w,r)

