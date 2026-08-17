# Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String
def strings(str):
    count1=0
    for i in str:
        if(i==" "):
            count1+=1
    print(f'The total words in string {count1+1}')
    count2=0
    for i in str:
        count2+=1
    print(f'The total characters in string {count2}')

str=(input('Enter string:'))
strings(str)