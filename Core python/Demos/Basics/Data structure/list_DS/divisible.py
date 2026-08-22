li=[25,6,79,28,3,76]
m=int(input('Enter value for m:'))
n=int(input('Enter value for n:'))
for i in range(0,len(li)):
    if(li[i]%m==0 and li[i]%n==0):
        print(li[i])
