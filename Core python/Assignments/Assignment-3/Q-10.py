# WAP to check if person is eligible to marry or (male age>=21 and female age>=18)
# take input age
gender=(input('Enter gender(m/f):'))
age=int(input('Enter age:'))
if(gender=='m'):
    if(age>=21):
        print('you are eligible for marry')
    else:
        print('you are not eligible for marry')
else:
    if(age>=18):
        print('you are eligible for marry')
    else:
        print('you are not eligible for marry')