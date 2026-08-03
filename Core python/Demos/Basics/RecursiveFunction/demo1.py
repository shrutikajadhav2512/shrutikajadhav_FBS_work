def series(n):
    if(n>0):
        print(n)
        series(n-1)
n=int(input('enter a number:'))
series(n)