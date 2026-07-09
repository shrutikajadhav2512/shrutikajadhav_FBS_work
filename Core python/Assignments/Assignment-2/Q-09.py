# Write a program to swap two numbers without using third variable
# take input for two numbers
num1=int(input('Enter first number:'))
num2=int(input('Enter second number:'))
# calculations
num1=num1+num2 
num2=num1-num2
num1=num1-num2
# display
print(f'swap two numbers without third variable:{num1},{num2} ')
print(f'num1:{num1},num2:{num2}')