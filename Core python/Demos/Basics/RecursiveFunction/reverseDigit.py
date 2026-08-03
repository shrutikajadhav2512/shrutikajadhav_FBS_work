# reverse digit using recursion
def reverse(n,rev=0):
    if(n>0):
        d=n%10
        rev=rev*10+d
        return reverse(n//10,rev)
    else:
        return rev
n=int(input('Enter a number:'))
res=reverse(n)
print(res)