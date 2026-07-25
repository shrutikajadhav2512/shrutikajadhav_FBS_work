# WAP to print armstong number within a given range 
startnum=int(input('Enter the starting number for range:'))
endnum=int(input('Enter the ending number for range:'))
print(f'{startnum} to {endnum} armstrong number.')
for no in range(startnum,endnum+1):
    temp=no
    total=0
    count=len(str(no))
    while(temp>0):
        d=temp%10
        total=total+(d**count)
        temp=temp//10

    if(total==no):
        print(no)
    

  
