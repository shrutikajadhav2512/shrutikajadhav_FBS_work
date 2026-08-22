def lists(li):
    li2=[]
    for i in li:
        if(i not in li2):
            li2+=[i]
    print(li2)

li=[1,2,3,1,4,2,1,2]
lists(li)