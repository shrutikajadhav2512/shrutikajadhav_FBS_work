li=[66,24,89,65,34,76,90]
max=li[0]
for ind in range(1,len(li)):
    if(li[ind]>max):
        max=li[ind]
print('Maximum number in list:',max)