# WAP to print all numbers in a range divisible by a given range
starting=int(input('Enter starting number for range:'))
ending=int(input('Enter ending number for range:'))
num=int(input('enter number divisible:'))
for i in range(starting,ending):
    if(i%num==0):
        print(i)
