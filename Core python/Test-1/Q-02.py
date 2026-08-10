# Write a program to calculate simple interest based on Principal, Rate and Time
# (SI = P*R*T/100)
def simpleInterest(p,r,t):
    si=(p*r*t)/100
    amount=p+si
    print(f'simple interest is {amount}')

p=int(input('enter principal amount:'))
r=int(input('enter rate:'))
t=int(input('enter time:'))
simpleInterest(p,t,r)