# Python Program to Check if a Given Key Exists in a Dictionary or Not
def dictionary(di):
    key=input("Enter key:")
    if(key in di):
        return True
    else:
        return False
di={'name':'abc','salary':50000,'dept':'IT'}
res=dictionary(di)
print(res)