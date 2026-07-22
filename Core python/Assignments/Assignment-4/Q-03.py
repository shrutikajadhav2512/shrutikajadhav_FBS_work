# WAP to print sum of series upto n.
# take input from user for n number
num=int(input('Enter a number:'))
sum=0
for i in range(1,num+1):
    sum=sum+i
print(f'1 to {num} sum={sum}')