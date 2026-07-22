start_no=int(input('Enter staring no:'))
end_no=int(input('Enter ending no:'))
for i in range(start_no,end_no):
    if(i%2==0):
        print(f'even{i}')
    if(i%2!=0):
        print(f'odd{i}')

