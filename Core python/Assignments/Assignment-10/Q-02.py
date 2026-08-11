# WAP to find maximum and minimum element in a list.
def maxMin(li):
    max=li[0]
    min=li[0]
    for i in range(0,len(li)):
        # find maximum element in list
        if(max<li[i]):
            max=li[i]
        # find minimum element in list
        if(min>li[i]):
            min=li[i]
    print(f'maximum element in list is {max}')
    print(f'minimum element in list is {min}')
li=[22,12,155,111,13,334]
maxMin(li)
