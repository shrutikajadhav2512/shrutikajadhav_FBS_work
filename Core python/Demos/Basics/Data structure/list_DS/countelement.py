def lists(li,n):
    count=0
    for i in range(0,len(li)):
        if(li[i]==n):
            count+=1
    print(count)

li=[1,2,3,45,1,2,3,4,1,4,1]
n=int(input('Enter a number:'))
lists(li,n)