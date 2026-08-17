# Python Program to Calculate the Length of a String Without Using a
# Library Function
def length(str):
    count=0
    for i in str:
        count+=1
    print(count)

str=(input('Enter string:'))
length(str)