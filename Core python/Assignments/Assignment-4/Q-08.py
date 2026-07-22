# WAP to find which numbers are divisible by 7 and multiple of 5 in a given range
starting=int(input('Enter a staring value:'))
ending=int(input('Enter a ending value:'))
print('divisible by 7 and multiple of 5')
for i in range(starting,ending+1):
    if(i%7==0 and i%5==0):
        print(i)
