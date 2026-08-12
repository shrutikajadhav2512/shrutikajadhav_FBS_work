# Python Program to Sort the List According to the Second Element in Sublist.
def lists(li):
    for i in range(len(li)):
        for j in range(0,len(li)-i-1):
            if(li[j][1]>li[j+1][1]):
                li[j],li[j+1]=li[j+1],li[j]
    print(f'after sorting list {li}')
li=[[10,56],[5,4],[50,60],[25,12]]
print(f'list {li}')
lists(li)
