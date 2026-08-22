def linearSearch(li,search_ele):
    for ind in range(0,len(li)):
        if(li[ind]==search_ele):
            return ind
    else:
        return -1
ele=int(input('enter element to find:'))
li=[45,26,88,75,19,90]
res=linearSearch(li,ele)
if(res!=-1):
    print(f'{ele} is present at index {res}')
else:
    print(f'{ele} is not present in list {res}')
