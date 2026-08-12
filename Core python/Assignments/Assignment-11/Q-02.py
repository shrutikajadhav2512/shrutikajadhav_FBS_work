# Python Program to Merge Two Lists and Sort it
def merge(li1,li2):
    li3=li1+li2
    print(f'merge list1 and list2 = list3 {li3}')
    li3.sort()
    print(f'sort list3 : {li3}')

li1=[100,200,1000,50,250]
li2=[50,30,1200,60,498]
print(f'list1 {li1}')
print(f'list2 {li2}')
li3=[]
result=merge(li1,li2)
