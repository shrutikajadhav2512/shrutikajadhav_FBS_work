# Python Program to Replace all Occurrences of ‘a’ with $ in a String
def replace(str):
    str2=""
    for i in str:
        if(i=="a"):
            str2+="$"
        else:
            str2+=i
    print(str2)

str=(input('enter string:'))
replace(str)