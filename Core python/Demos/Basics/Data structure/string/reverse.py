def reverseString(str1):
    rev=""
    for i in range(len(str1)-1,-1,-1):
        rev+=str1[i]
    print(rev)

str1="sachin"
reverseString(str1)