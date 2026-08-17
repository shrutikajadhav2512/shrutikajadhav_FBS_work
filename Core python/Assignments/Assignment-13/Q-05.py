# Python Program to Sum All the Items in a Dictionary
def dictionary(di):
    addition=0
    for value in di.values():
        addition+=value
    print(f'values addition:{addition}')

di={1:20,2:30,5:40,4:500}
dictionary(di)