li=[1,2,3,4,5,6,7,8,9,10]
# Traditional
li2=[]
for i in li:
    if(i%2==0):
        li2.append("even")
    else:
        li2.append("odd")
print(li2)
# comprehension
li2=["Even" if i%2==0 else "odd" for i in li]
print(li2)
# comprehension
li3=[2,3,4,5]
li4={i:i**2 for i in li3}
print(li4)
    
