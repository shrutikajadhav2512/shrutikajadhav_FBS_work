# Python Program to count number of lowercase characters in a string.
def string(str):
    count=0
    for i in str:
        if(i.islower()):
            count+=1
    print(f'lower case count is {count}')


str=input('Enter string:')
string(str)