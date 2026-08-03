def palindrome(num):
    temp=num
    rev=0
    while(temp>0):
        d=temp%10
        rev=rev*10+d
        temp=temp//10
    if(num==rev):
        return True
    else:
        return False
data=[121,10,545,7,333,876]
res=list(map(palindrome,data))
print(res)
