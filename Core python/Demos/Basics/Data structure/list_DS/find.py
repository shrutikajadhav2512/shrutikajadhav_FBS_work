def findElement(li,n):
    for i in li:
        if(i==n):
            return i
    else:
        return -1

li=[10,15,20,35,30,25]
n=int(input("enter the number,then will check in this list: "))
print(li)
res=findElement(li,n)
if(res!=-1):
    print('Element present in this list')
else:
    print('Element not present in this list')