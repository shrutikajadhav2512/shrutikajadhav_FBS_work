# Python Program to Find the Intersection of Two Lists
def interSection(li1,li2):
    intersection=[]
    for i in li1:
        if(i in li2):
            intersection.append(i)
    print(f'Inter Section list {intersection}')

li1=[1,2,5,3,6,2,3,4]
li2=[2,7,9,0,2,4,3]
print(f'list 1 {li1}')
print(f'list 2 {li2}')
interSection(li1,li2)