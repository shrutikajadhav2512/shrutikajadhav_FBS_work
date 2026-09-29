# Remove all of the vowels in a string (take input from user)
a=input("Enter string:")
x=[i for i in a if(i!="A")and(i!="a")and(i!="e")and(i!="E")and(i!="i")and(i!="I")and(i!="o")and(i!="O")and(i!="u")and(i!="U")]
for i in x:
    print(i,end=" ")
