# Python Program to Remove the Given Key from a Dictionary
def dictionary(key,di):
    di2={}
    for i in di:
        if(i!=key):
            di2[i]=di[i]
    print(di2)

di={'id':101,'name':'abc','dept':'CS'}
key=input("Enter a key you want to delete:")
dictionary(key,di)