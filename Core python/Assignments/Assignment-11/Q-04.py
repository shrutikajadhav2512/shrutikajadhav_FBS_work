# Python Program to Find the Second Largest Number in a List Using Bubble
# Sort
def secondLargest(li):
    for i in range(1,len(li)):
        for j in range(0,len(li)-1):
            if(li[j]>li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]
                
    print(f'After sorting:{li}')
    print(f'second largest element:',li[-2])

li=[100,40,80,555]
print(li)
secondLargest(li)