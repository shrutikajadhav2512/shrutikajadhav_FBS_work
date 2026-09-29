# Develop a memoization decorator that caches the results of function
# calls and returns the cached result when the same inputs occur again.
# This can greatly improve the performance of recursive or
# computationally intensive functions.
def memoize(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper
@memoize
def square(n):
    print("Calculating...")
    return n * n
print(square(5))
print(square(5))
print(square(10))
