# WAP to print list after removing even numbers.
def lists(li):
    res=list(filter(lambda i:i%2!=0,li))
    print(f'after removing even numbers:{res}')
            
li=[1,2,3,4,5,6,7,8,9]
print(f'list {li}')
lists(li)