# Python Program to Multiply All the Items in a Dictionary
def multiplyValues(di):
    multiply=1
    for value in di.values():
        multiply*=value
    print(f'Multiply all dictionary values {multiply}')

di={1:10,2:30,3:40,5:40}
multiplyValues(di)