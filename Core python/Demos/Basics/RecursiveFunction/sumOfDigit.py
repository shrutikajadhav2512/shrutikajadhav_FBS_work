# sum of digit using recursive function
def digit(n):
    if(n>0):
        d=n%10
        return d + digit(n//10)
    else:
        return 0
n=int(input('Enter a number:'))
res=digit(n)
print(f'sum of digit={res}')