# WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic
# da=10% of basic,ta=12% of basic, hra=15% of basic.
# take input for salary
salary=float(input('enter salary:'))
# calculations
da=salary*0.10
ta=salary*0.12
hra=salary*0.15
total=salary+da+ta+hra
print(f'total salary is:{total}')