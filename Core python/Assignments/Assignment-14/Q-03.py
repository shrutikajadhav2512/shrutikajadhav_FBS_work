# Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.
def demo(a,b):
    for i in b:
        print(i, "=", a.count(i))
a = ["apple", "banana", "apple", "mango", "banana", "apple"]
b = set(a)
demo(a,b)