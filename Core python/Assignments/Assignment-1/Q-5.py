# WAP to enter P,T,R and calculate compound interest.
# take input for compound interest(P,T,R)
P=int(input('Enter principal amount:'))
R=int(input('Enter rate of interest:'))
T=int(input('Enter time in years:'))
# calculation
A=P*(1+R/100)**T
CI=A-P
# display result

print(f'compound interest is:{CI}')