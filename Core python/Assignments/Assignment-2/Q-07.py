# Find the sum of three-digit number
# take three digit number
x=int(input('Enter three digit number:'))
# calculations
digit1=x%10 
num=x//10
digit2=num%10
num=num//10
digit3=num%10
num=num//10
sum=digit1+digit2+digit3
print(f'sum of three digit number:{sum}')


