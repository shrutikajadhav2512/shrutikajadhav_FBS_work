# WAP to print all numbers which are 
# divisible by m and n in the list.
def divisible(li,m,n):
    for i in range(0,len(li)):
        if(li[i]%m==0 and li[i]%n==0):
            print(f'Divisible by {m} and {n}={i}:{li[i]}')
li=[25,20,27,26,30]
m=int(input('Enter first divisible number:'))
n=int(input('Enter second divisible number:'))
divisible(li,m,n)
