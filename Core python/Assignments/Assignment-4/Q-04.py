# WAP to print factorial of a number
# take number form user for fact
num=int(input('Enter number for factorial:'))
fact=1
i=1
while(i<=num):
    fact=fact*i
    i+=1
print(f'factorial={fact}')
   