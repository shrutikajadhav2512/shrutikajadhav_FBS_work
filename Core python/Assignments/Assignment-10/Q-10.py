# WAP to remove all occurrences of a given element in the list.
def occurrences(li,num):
    li2=[]
    for i in li:
        if(i!=num):
            li2=li2+[i]
        
    print(f'Remove all occurrences {li2}')

li=[1,3,6,2,6,8,3,6,9]

num=int(input('Enter number for remove all occurrences:'))
print(f'list {li}')
occurrences(li,num)