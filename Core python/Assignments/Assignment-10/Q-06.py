# WAP to remove duplicates from the list.
def removeDuplicate(li):
    li2=[]
    for i in li:
        if(i not in li2):
            li2=li2+[i]
    print(f'remove duplicates {li2}')
li=[1,2,3,1,4,5,1,5,2]
print(f'list {li}')
removeDuplicate(li)