no=int(input('enter no:'))
row=int(input('enter row:'))
column=int(input('enter column:'))
for i in range(1,row):
    for j in range(1,column):
        print(i*no,end=' ')
    print()