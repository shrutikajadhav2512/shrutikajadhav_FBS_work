# WAP to create a duplicate of an existing list. It should not point to
# same list.
def lists(li1):
    li2=[]
    for i in li1:
        li2+=[i]
    print(f'duplication list(list2) {li2}')
    li2+=[10]
    print(f'duplication list and add one element{li2}')

li1=[90,80,70,60,50]
print(f'list1 {li1}')
lists(li1)