# We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.
end = int(input("Enter ending number: "))
def fibonacci(end):
    a = 0
    b = 1
    while a <= end:
        yield a
        a, b = b, a + b
x = fibonacci(end)
for i in x:
    print(i)

    
