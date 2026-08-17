# Python Program to Concatenate Two Dictionaries Into One
def dictionary(di1,di2):
    # di3={}
    # di3=di1|di2
    di3={}
    for key,value in di1.items():
        if(key,value not in di3):
            di3[key]=value
    for key,value in di2.items():
        if(key,value not in di3):
            di3[key]=value
    print(di3)

di1={'name':'abc','number':123,'city':'pune'}
di2={'education':'graduate','marks':90,'college':'pune'}
dictionary(di1,di2)
