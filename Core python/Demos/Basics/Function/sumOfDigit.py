# sum of digit
def digit():
    no=int(input('enter number:'))
    sum=0
    temp=no
    while(temp>0):
        d=temp%10
        temp=temp//10
        sum=sum+d
    print(f'sum of digit={sum}')
digit()