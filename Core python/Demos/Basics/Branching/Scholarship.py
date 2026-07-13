# Student scholarship based on marks
# take input marks
marks=float(input('Enter marks:'))

# condition
if(marks>=75):
    income=float(input('Enter income:'))
    if(income <= 100000):
        print('Full scholarship')
    else:
        print('50% Scholarship')
else:
    print('No Scholarship')
    