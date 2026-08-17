# Python Program to find larger string without using built-in functions.
def large(str1,str2):
    count1=0
    for i in str1:
        count1+=1
    print(f'first string count {count1}')
    count2=0
    for i in str2:
        count2+=1
    print(f'second string count {count2}')
    if(count1>count2):
        print('first string is large.')
    elif(count2>count1):
        print('second string is large.')
    else:
        print('both string is same.')

str1=(input('enter first string:'))
str2=(input('enter second string:'))
large(str1,str2)