# WAP to reverse the list.
def rev(li,li2):
    print('Before reverse:',li)
    res=li[::-1]
    print(f'After reverse:{res}')
    print()
    print('Before reverse:',li2)
    res=li2[::-1]
    print(f'After reverse:{res}')
li=[10,30,50,70,90]
li2=[90,80,70,60,50]
rev(li,li2)
