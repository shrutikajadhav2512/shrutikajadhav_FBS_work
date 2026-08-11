# WAP of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.
def number(li):
    li2=[]
    li3=[]
    for i in li:
        if(i%2==0):
            li2=li2+[i]
        else:
            li3=li3+[i]
    print('Even number list:',li2)
    print('Odd numbar list:',li3)
li=[1,2,3,4,5,6,7,8,9,10]
print('list=',li)

number(li)
