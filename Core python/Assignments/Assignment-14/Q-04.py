# Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.
def demo(a,n):
    for x in a:
        for y in a:
            if(x + y == n):
                print(x, y)
    else:
                print("invalid input")
a=[2, 4, 5, 7, 8]
n=int(input("Enter a number:")) 
demo(a,n)
