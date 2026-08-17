# Python Program to Take in a String and Replace Every Blank Space
# with Hyphen
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