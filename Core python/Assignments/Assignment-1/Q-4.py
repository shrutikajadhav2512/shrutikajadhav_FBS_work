# WAP to enter P,T,R and calculate simple interest
# take input for simple interest(P,T,R)
P=int(input('Enter principal amount:'))
R=int(input('Enter rate of interest:'))
T=int(input('Enter time in years:'))
# calculation
SI=P*R*T/100

# display result
print(f'simple interest is:{SI}')