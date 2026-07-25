# enter number of students from user.
# for those many students acccept marks
# of 5 subject marks from user and
# calculate percentage.display all percentage
# and average percentage of students.
num=int(input('enter the number of students:'))
for i in range(1,num+1):
    print('enter 5 sub marks')
    sub1=int(input('enter sub1 marks:'))
    sub2=int(input('enter sub2 marks:'))
    sub3=int(input('enter sub3 marks:'))
    sub4=int(input('enter sub4 marks:'))
    sub5=int(input('enter sub5 marks:'))
    total=sub1+sub2+sub3+sub4+sub5
    per=total/500*100
    avg=total/5
    print(f'total={total},parcantage={per},average={avg}')