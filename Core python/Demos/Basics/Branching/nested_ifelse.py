# eligible or not eligible for marriage
# take input
gender=input('enter gender(m/f):')
age=int(input('enter age:'))
if(gender=='f'):
    if(age>=18):
        print('eligible for marriage')
    else:
        print('pahle padhai kar lo') 
else:
    if(age>=21):
        print('eligible for marrige')
    else:
        print('pahle kama lo') 
