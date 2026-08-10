# Write a program to accept distance in km and convert it into meters and
# centimeters both.
def distance(km):
    meter=km*1000
    centimeter = km * 100000
    print(f'km into meter={meter}')
    print(f'km into centimeter={centimeter}')

km=float(input('enter distance in km:' ))
distance(km)
