def demo():
    for i in range(100,200):
        yield i
g=demo()
print(next(g))
print("next value..")
print(next(g))
print("next value..")
print(next(g))
print("next value..")
print(next(g))
print(".........")
list=(i for i in range(100,201))
print(next(list))
print(next(list))
print(next(list))
print(next(list))
print(next(list))
