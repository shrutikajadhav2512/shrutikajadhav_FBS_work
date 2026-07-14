# WAP to calculate profit or loss
# take input selling price and cost price
sp=int(input('Enter selling price:'))
cp=int(input('Enter cost price:'))

if(sp>cp):
    profit=sp-cp
    print(f'{profit}rs profit')
elif(cp>sp):
    loss=cp-sp
    print(f'{loss}rs loss')
else:
    print('no profit no loss')