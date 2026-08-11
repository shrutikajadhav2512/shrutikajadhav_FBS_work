#WAP to create a new list from existing list which contains cube of
# each number of list.
def cube(li):
    li2=[]
    for i in li:
        a=i**3
        li2=li2+[a]
    print(f'cube {li2}')
    
li=[1,2,3,4,5,6,7]
print('li=',li)
res=cube(li)
