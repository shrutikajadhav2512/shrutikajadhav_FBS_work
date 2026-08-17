# Python Program to Remove the Characters of Odd Index Values in a
# String
def strings(str1):
    str2=" "
    for i in range(0,len(str1)):
        if(i%2==0):
            str2+=str1[i]
            
    print(f'Remove the Characters of Odd Index Values:{str2}')

str1=(input('Enter string:'))
strings(str1)