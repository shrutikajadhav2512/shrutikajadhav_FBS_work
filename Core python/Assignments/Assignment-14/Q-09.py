# Write a Python program to find all the unique combinations of 3
#numbers from a given list of numbers, adding up to a target number.
def adding(a,target):
    for i in range(len(b)):
        for j in range(i+1,len(b)):
            for k in range(j+1,len(b)):
                if(b[i]+b[j]+b[k]==target):
                    print(b[i],b[j],b[k])
a={1,3,5,7,9,2}
b=list(a)
target=int(input('Enter your target:'))
adding(a,target)