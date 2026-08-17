# Python Program to Count the Number of Vowels in a String
def strings(str):
    count=0
    for j in str:
        if('a'==j or 'e'==j or 'i'==j or 'o'==j or 'u'==j or 'A'==j or 'E'==j or 'I'==j or 'O'==j):
            count+=1
    print(f'Total vovels count is {count} ')


str=(input('Enter string:'))
strings(str)