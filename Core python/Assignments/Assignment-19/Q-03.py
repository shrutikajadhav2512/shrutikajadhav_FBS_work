# Count the number of spaces in a string (take input from user)
a = input("Enter string:")
count = sum(1 for i in a if(i==" "))
print(count)
