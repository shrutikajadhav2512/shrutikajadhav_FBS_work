# Python Program to Find the Union of two Lists without
# using set concept.
li1=[1,2,3,4]
li2=[3,4,5,6]
li3=[]
for i in li1:
    li3+=[i]
for j in li2:
    if(j not in li3):
        li3+=[j]
print(li3)