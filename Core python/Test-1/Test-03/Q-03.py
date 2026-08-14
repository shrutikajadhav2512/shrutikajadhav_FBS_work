# Write a program to accept basic salary of n emp. (n should be
# accepted from user). If basic salary is below 20000 then
# da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and
# hra=20%. Based on this calculate the total salary of each emp
# and also total salary of all emp.
n=int(input('Enter employee:'))
total_emp=0
for i in range(1,n+1):
    salary=int(input("enter salary:"))
    if(salary<20000):
        da=salary*0.10
        ta=salary*0.12
        hra=salary*0.15
    else:
        da=salary*0.15
        ta=salary*0.18
        hra=salary*0.20
    total=salary+da+ta+hra
    total_emp=total_emp+total
    print(f"emp salary:{total}")
print(f"total emp salary:{total_emp}")
