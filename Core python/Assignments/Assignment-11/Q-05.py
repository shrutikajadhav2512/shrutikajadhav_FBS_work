# Python Program to Sort a List According to the Length of the Elements
# within the list.
def lists(li):
    for i in li:
        li.sort(key=len)
        
    print(f'sorted list {li}')

li=['python','c++','java','html','bootstrap']
lists(li)