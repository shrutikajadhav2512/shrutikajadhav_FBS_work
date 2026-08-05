# WAP to reverse a given number using recusive function.
def reverse(n,rev=0):
    if(n>0):
        d=n%10
        rev=rev*10+d
        return reverse(n//10,rev)
    else:
        return rev
n=int(input('Enter a number:'))
res=reverse(n)
print('reverse number is',res)