# WAP to print all odd number until n.
# take input from user for n 
num=int(input('Enter a number:'))
print(f'All odd number 1 to {num}')
for i in range(1,num):
    if(i%2!=0):
        print(i)