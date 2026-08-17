# Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).
def dictionary(n):
    di={}
    for x in range(1,n+1):
        di[x]=x*x
    print(di)

n=int(input('Enter number:'))
dictionary(n)