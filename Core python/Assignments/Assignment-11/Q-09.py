# WAP to create three lists of numbers, their squares and cubes
def lists(li):
    for i in li:
        a=i**2
        square.append(a)
        b=i**3
        cube.append(b)
    print(f'square is {square}')
    print(f'cube is {cube}')
        

li=[1,2,3,4,5]
print(f'list={li}')
square=[]
cube=[]
lists(li)