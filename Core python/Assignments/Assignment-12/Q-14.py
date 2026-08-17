# Python Program to count the occurrences of each word in a string.
def strings(str1):
    words = str1.split()
    count=0
    for i in words:
        if(i=='each'):
            count+=1
    print(f"count {count}")

str1=(input('enter string:'))
strings(str1)