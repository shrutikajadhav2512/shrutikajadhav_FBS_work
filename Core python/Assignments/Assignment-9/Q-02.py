# WAP to check if given number is armstrong or not
#  using recursive function
def armstrong(n,count,temp):
    if(n==0):
        return 0
    else:
        d=n%10
        return (d**count)+armstrong(n//10,count,temp)
    
n=int(input('enter the number:'))
count=len(str(n))
res=armstrong(n,count,n)
if(res==n):
    print(f'{n} is armstrong.')
else:
    print(f'{n} is not armstrong.')



