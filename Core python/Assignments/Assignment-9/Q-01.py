# Write a program to find sum of following 
# series using recursive functions:

# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions

def factorial(n):
    if(n>0):
        return n*factorial(n-1)
    else:
        return 1
def add(n):
    if(n>0):
        return factorial(n)+add(n-1)
    else:
        return 0
n=int(input('enter the number:'))
res=add(n)
print(f'1! + 2! + 3! + .... + n! sum of series 1 to {n}:{res}')