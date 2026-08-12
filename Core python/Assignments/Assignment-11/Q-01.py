# Python Program to Put Even and Odd elements of a List into two Different Lists
def evenOdd(li):
    odd=[]
    even=[]
    for i in li:
        if(i%2==0):
            even+=[i]
        else:
            odd+=[i]
    print(f'Even number list {even}')
    print(f'Odd number list {odd}')
li=[1,2,3,4,5,6,7,8,9]
print(f'list {li}')
evenOdd(li)
