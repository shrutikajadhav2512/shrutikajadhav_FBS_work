# WAP to find sum of all elements of list.
def additionList(li):
    sum=0
    for i in range(0,len(li)):
        sum=sum+li[i]
    return sum
li=[5,4,1,9,2,4,0]
res=additionList(li)
print(f'sum of all elements in list={res}')