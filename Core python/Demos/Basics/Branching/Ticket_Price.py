# ticket price
# take input age for ticket price
age=int(input('Enter age:'))
# condition
if(age<=5):
    print(f'Ticket Free')
else:
    if(age<=18):
        print(f'100rs')
    else:
        print(f'200rs')
