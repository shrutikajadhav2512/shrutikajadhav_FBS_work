def demo():
    yield(10)
    yield(20)
    yield(30)
g=demo()
print(next(g))
print("Next value..")
print(next(g))
