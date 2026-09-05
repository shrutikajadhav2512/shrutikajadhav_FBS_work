start=int(input("enter starting no:"))
end=int(input("enter ending no:"))
# li=[]
# for i in range(start,end+1):
#     if(i%2!=0):
#         li.append(i**2)
# print(li)

li2=[i**2 for i in range(start,end+1) if i%2!=0]
print(li2)

