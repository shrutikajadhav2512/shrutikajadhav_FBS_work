# Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged.
def exchange(str):
    a=str[1:len(str)-1]
    print(str[-1]+a+str[0])

str=(input('Enter string:'))
exchange(str)