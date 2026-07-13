# find the Grade
# take input marks
marks=float(input('Enter ur marks:'))
# branching and display
if(marks>=75):
    print('Distinction')
elif(marks>=60):
    print('1st class')
elif(marks>=50):
    print('2nd class')
elif(marks>=35):
    print('Pass')
else:
    print('Fail')