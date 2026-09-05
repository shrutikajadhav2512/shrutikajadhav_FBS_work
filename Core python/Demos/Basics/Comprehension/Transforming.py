li=[1,2,3,4,5,6,7,8,9,10]

li2=[x for x in li]
print(li2)

li2=[x*10 for x in li]
print(li2)

li2=[x*x for x in li]
print(li2)

li2=[x**3 for x in li]
print(li2)

start=int(input("Enter starting no:"))
end=int(input("Enter ending no:"))
li5=[x**0.5 for x in range(start,end)]
print(li5)


