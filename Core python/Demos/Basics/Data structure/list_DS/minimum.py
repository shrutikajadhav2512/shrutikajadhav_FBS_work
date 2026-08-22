# find minimun value in list
li=[25,12,20,4,50,1]
mini=li[0]
for i in range(1,len(li)):
    if(mini>li[i]):
        mini=li[i]
print(f'Minimum value in list is {mini}')