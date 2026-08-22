# Write a Python program to find elements in a given set that are not in
# another set.
def demo(set1,set2):
    set3=set()
    for i in set1:
        if(i not in set2):
            set3.add(i)
    print(set3)
set1={10,20,30,40,600}
set2={10,30,50,60}
demo(set1,set2)