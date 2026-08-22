# Write a Python program to remove the intersection of a second set
# with a first set.
def intersection(a,b,c):
    for i in a:
        if(i not in b):
            c.add(i)
    print(c)

a = {1,2,3,4,5,8}
b = {3,4,5,6,7}
print(a)
print(b)
c=set()
intersection(a,b,c)