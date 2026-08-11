# WAP to print list after removing even numbers.
def even(li):
    li2=[]
    for i in li:
        if(i%2!=0):
            li2+=[i]
    print(f'remove even numbers:{li2}')

li=[1,2,3,4,5,6,7,8,9,10]
print('li=',li)

even(li)
