# prime no from user range
Starting=int(input('enter starting no:'))
Ending=int(input('enter ending no:'))

for num in range(Starting,Ending//2+1):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)
    else:
        print('number is not prime nor composite')