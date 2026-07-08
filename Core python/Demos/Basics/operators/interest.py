# take input for simple interest (P,T,R)
P=int(input('Enter principal amount:'))
R=int(input('Enter rate of interest:'))
T=float(input('Enter time in yr:'))
# calculation
Simple_interest=P*(R/100)*T
# display result
print(f'simple interest is:{Simple_interest}')