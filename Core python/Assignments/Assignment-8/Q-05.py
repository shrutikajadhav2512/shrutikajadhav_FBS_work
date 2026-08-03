# sum of all prime numbers between 1 to n 
def prime(n):
    sum=0
    for num in range(2,n+1):
        if(num>1):
            for i in range(2,num):
                if(num%i==0):
                    break
            else:
                print(num)
                sum=sum+num
    return sum
    
n=int(input('Enter number:'))
result=prime(n)
print(f'sum of prime number 1 to {n} = {result}')
