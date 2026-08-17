# Python Program to count number of digits and letters in a string.
def string(str):
    count=0
    for i in str:
        if(i.isalpha()):
            count+=1
    print(f'Total letters={count}')
    count=0
    for i in str:
        if(i.isdigit()):
            count+=1
    print(f'Total digit={count} ')

str=(input('Enter string:'))
string(str)