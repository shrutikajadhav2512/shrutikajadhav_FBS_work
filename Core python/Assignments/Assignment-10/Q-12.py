# Write a program to create three lists of numbers, their squares
# and cubes
def lists(li):
    square=[]
    cube=[]
    for i in li:
        a=i**2
        square+=[a]
        b=i**3
        cube+=[b]
    print(f'square list {square}')
    print(f'cube list {cube}')
li=[1,2,3,4,5]
print(f'list {li}')
lists(li)