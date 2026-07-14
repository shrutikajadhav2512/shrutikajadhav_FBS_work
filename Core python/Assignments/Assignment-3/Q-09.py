# input 5 suject marks from user and display grade(eg,first class,secend class...)
# take input 5 subject marks
sub1=int(input('Enter marks subject1:'))
sub2=int(input('Enter marks subject2:'))
sub3=int(input('Enter marks subject3:'))
sub4=int(input('Enter marks subject4:'))
sub5=int(input('Enter marks subject5:'))

# calculations
total=sub1+sub2+sub3+sub4+sub5
per=total/500*100
print(f'total:{total}')
print(f'percentage:{per}')

if(per>=75):
    print(f'{per} Distinction')
elif(per>=60):
    print(f'{per} First class')
elif(per>=50):
    print(f'{per} Second class')
elif(per>=35):
    print(f'{per} Pass')
else:
    print(f'{per} Fail')