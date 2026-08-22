def strings(str):
    str2=""
    for i in str:
        if(i==" "):
            str2+="@"
        else:
            str2+=i
    print(str2)
str=(input('enter string:'))
strings(str)