# WAP to print fibonacci series upto n
fibo=int(input('Enter number for fibonacci:'))
print(f'fibonacci series 1 to {fibo}')
a=-1
b=1
for i in range(fibo+1):
    c=a+b
    print(c)
    a=b
    b=c
