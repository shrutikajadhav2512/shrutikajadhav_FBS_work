# Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.
def number(n,li):
    # find count
    count=0
    for num in li:
        if(n==num):
            count+=1
    return count
n=int(input('Enter a number:'))
li=[5,20,15,30,25,40,35,40,35,40]
res=number(n,li)
if(res!=0):
    print(f'{n} is present in the list')
    print(f'{n} is {res} times')
else:
    print(f'{n} is not present in the list')