# WAP to calculate the percentage of student based on marks of any 5 subjects.
# Take 5 subject marks
sub1=int(input('Enter sub1 marks:'))
sub2=int(input('Enter sub2 marks:'))
sub3=int(input('Enter sub3 marks:'))
sub4=int(input('Enter sub4 marks:'))
sub5=int(input('Enter sub5 marks:'))
#Calculations
total=sub1+sub2+sub3+sub4+sub5
percentage=total/500*100
# Display
print(f'Marks:{sub1},{sub2},{sub3},{sub4},{sub5}')
print(f'Total marks:{total}')
print(f'Percentage:{percentage}')


