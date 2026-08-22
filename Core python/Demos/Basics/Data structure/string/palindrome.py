def palindrome(n):
    left=0
    right=len(n)-1
    palin=True
    while(left<right):
        if(n[left]!=n[right]):
            palin=False
            break
        left+=1
        right-=1
    return palin
n=(input('Enter string for check palindrome or not:'))
res=palindrome(n)
print(res)
if(res):
    print(f'{n} palindrome')
else:
    print(f'{n} not palindrome')
