# Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.
def compared(a,b):
    c=set()
    for i in a:
        if(i not in b):
            c.add(i)
    print(c)
    d=set()
    for j in b:
        if(j not in a):
            d.add(j)
    print(d)
a={1,2,3,4}
b={1,3,4,5}
compared(a,b)