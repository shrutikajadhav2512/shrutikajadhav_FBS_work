# Python Program to Find the Union of two Lists
def unionList(li1,li2):
    union=[]
    for i in li1:
        union+=[i]
    for i in li2:
        union+=[i]
    print(f'union list {union}')

li1=[90,80,70,60]
li2=[40,30,20,10,5]
print(f'list 1 {li1}')
print(f'list 2 {li2}')
unionList(li1,li2)