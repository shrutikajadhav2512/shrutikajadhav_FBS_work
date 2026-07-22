# WAP to print check if a given range is prime number or not
starting=int(input('Enter starting number:'))
ending = int(input('Enter ending number: '))
for num in range(starting,ending):
    if(num>1):
        for i in range(2,num):
            if(num % i == 0):
                break
        else:
            print(num)
    else:
        print('the number is not prime number nor composite')