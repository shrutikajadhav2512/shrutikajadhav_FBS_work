# Python Program to Remove the nth Index Character from a Non-Empty
# String
def character(str):
    if(0<=num<(len(str))):
        res=str[:num]+str[num+1:]
        print(res)
    else:
        print('invalid  index')

str=(input('Enter string:'))
num=int(input('Enter a number then will remove nth index:'))
character(str)