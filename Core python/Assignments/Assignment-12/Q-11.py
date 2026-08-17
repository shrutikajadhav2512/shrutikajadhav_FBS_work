# Python Program to replace every blank space with hyphen in a string.

def strings(str):
    str2=""
    for i in str:
        if(i==" "):
            str2+="-"
        else:
            str2+=i
    print(str2)
str=(input('Enter string:'))
strings(str)