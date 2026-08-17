# Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions
def strings(str1,str2):
    count1=0
    for i in str1:
        count1+=1
    a=count1
    count2=0
    for i in str2:
        count2+=1
    b=count2
    if(a>b):
        print(f'string 1 is large,total count is {count1}.')
    elif(a<b):
        print(f'string 2 is large,total count is {count2}.')
    else:
        print(f'Both strings are same count.')


str1=(input('Enter string 1:'))
str2=(input('Enter string 2:'))
strings(str1,str2)